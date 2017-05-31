from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F, FloatField, Sum
from website.models import Order, UserOrder, Product


# invoked if there are no completed orders. it facilitates the display of a "no order" page.
@login_required
def display_order(request, order_id):
    '''
      purpose: Show the selected order with it's products and the total price of the function.

      author: Justin Short

      args: request, order_id

      returns: (render): a view of the request, template to use, and order oject
    '''
    # If trying to view, render product corresponding to id passed
    if request.method == "GET":

        # GET the users selected order
        target_order = Order.objects.get(pk=order_id)

        # Get the UserOrder for the user and selected object
        all_products = UserOrder.objects.all().filter(order=target_order)

        # Calculate the sum of all products costs and assign to total
        total = all_products.aggregate(total_price=Sum('product__price'))

        template_name = 'orders/display_order.html'
        return render(request, template_name, {"target_order": target_order, "all_products": all_products, "total": total["total_price"]})
