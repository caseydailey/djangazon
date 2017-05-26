# bring in the magic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

# import forms and models form this app
from website.models import Order, UserOrder

@login_required
def view_order(request):
    """
    purpose: present user order and handle interaction with cart

    author: casey dailey,  justin short, taylor perky

    args: request, order_id

    returns: 
    """
    # get user's open order and a reference to the products on it.
    try:
        open_order = Order.objects.get(buyer=request.user, date_complete__isnull=True)        
        products = UserOrder.objects.filter(order=open_order.id)

        # if GET and they have products, display them
        if request.method == 'GET' and products:
            template_name = 'orders/view_order.html'
            return render(request, template_name, {
                "products": products})

        # if deleting and they have at least one left, get that product and delete it
        elif 'delete' in request.POST and products:
            product1 = UserOrder.objects.get(pk=request.POST.get("product"))
            product1.delete()
            return HttpResponseRedirect('/view_order')

        # if no products, redirect to no_products
        elif not products:
            open_order.delete()
            return HttpResponseRedirect('/no_order')

        elif 'cancel_order' in request.POST:
            open_order.delete()
            return HttpResponseRedirect('/no_order')

        # redirect to checkout
        elif 'checkout' in request.POST:
            return HttpResponseRedirect('/view_checkout/{}'.format(open_order.id))

    # if there was no order
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/no_order')

