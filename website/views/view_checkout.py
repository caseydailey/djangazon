# bring in the magic
import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

# import forms and models form this app
from website.models import Product, PaymentType, Order, UserOrder

@login_required
def view_checkout(request, order_id):
    """
    purpose: display a user's order and handle actions handle checkout (apply a payment type)

    args: request, order_id (integer): the particular order being viewed

    returns: render display of products and payment types associated with a user and various redirects
    """
    # get products and payment types associated with order/user.
    products = UserOrder.objects.filter(order=order_id)
    payment_types = PaymentType.objects.filter(user=request.user)

    # if attempting to view the page and they have products and payment types, display them
    if request.method == 'GET' and products and payment_types:

        template_name = 'orders/view_checkout.html'
        return render(request, template_name, {
            "products": products,
            "payment_types": payment_types})

    # if attempting to checkout and they have products and payment types,
    elif request.method == 'POST' and products and payment_types:
        
        # get the payment type selected 
        # get the order
        payment_type = PaymentType.objects.get(pk=request.POST.get('select'))
        order = Order.objects.get(pk=order_id)
        order_receipt = UserOrder.objects.filter(order=order)

        order_quantities = dict()
        for instance in order_receipt:
            try: 
                order_quantities[instance.product.id].append(instance.product)
            except KeyError:
                order_quantities[instance.product.id] = list()
                order_quantities[instance.product.id].append(instance.product)

        #make sure there are enough of given product available before checkout
        check_for_below_zero_values = dict()
        for key, value in order_quantities.items():
            product = Product.objects.filter(pk=key)
            product_quantity = product.values('quantity')
            check_for_below_zero_values[key] = product_quantity[0]['quantity'] - len(value)

            # if there won't be enough, let the customer know
            if check_for_below_zero_values[key] < 0:
                messages.info(request, 
                    """Sorry, but we do not have enough {} for you to finish your order!! 
                       You currently have {} in your shopping cart,
                       but we only have {} available! 
                       Please adjust your order and try again.""".format(product[0].title, len(value), product_quantity[0]['quantity']))

                return render(request, 'wrong_product_quantity.html')

        
        # update quantities
        for key, value in check_for_below_zero_values.items():
            product = Product.objects.get(pk=key)
            product.quantity = value
            product.save()

        # finish this order by applying a payment_type and date_complete
        order.payment_type = payment_type
        order.date_complete = datetime.datetime.now()
        order.save()
        return HttpResponseRedirect('/order_complete/{}'.format(order_id))

    # if no products, redirect to no_order.html
    elif not products:
        return HttpResponseRedirect('/no_order')

    # if no payment types, redirect to no_payment types
    elif not payment_types:
        return HttpResponseRedirect('/no_payment_type')
