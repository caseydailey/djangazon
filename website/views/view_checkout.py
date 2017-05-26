# bring in the magic
import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# import forms and models form this app
from website.models import Product, PaymentType, Order

@login_required
def view_checkout(request, order_id):
    """
    purpose: display a user's order and handle actions handle checkout (apply a payment type)

    args: request, order_id (integer): the particular order being viewed

    returns: render display of products and payment types associated with a user and various redirects
    """
    # get products and payment types associated with order/user.
    products = Product.objects.filter(order=order_id)
    payment_types = PaymentType.objects.filter(user=request.user)

    # if attempting to view the page and they have products and payment types, display them
    if request.method == 'GET' and products and payment_types:

        template_name = 'orders/view_checkout.html'
        return render(request, template_name, {
            "products": products,
            "payment_types": payment_types})

    # if attempting to checkout and they have products and payment types,
    # get the payment type instance selected and apply it to the order along with a time stamp.
    elif request.method == 'POST' and products and payment_types:
        payment_type = PaymentType.objects.get(pk=request.POST.get('select'))
        user_order = Order.objects.get(pk=order_id)
        user_order.payment_type = payment_type
        user_order.date_complete = datetime.datetime.now()
        user_order.save()
        return HttpResponseRedirect('/order_complete/{}'.format(order_id))

    # if no products, redirect to no_order.html
    elif not products:
        return HttpResponseRedirect('/no_order')

    # if no payment types, redirect to no_payment types
    elif not payment_types:
        return HttpResponseRedirect('/no_payment_type')
