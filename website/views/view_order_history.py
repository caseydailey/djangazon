from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from website.models import Order, UserOrder


# invoked if there are no completed orders. it facilitates the display of a "no order" page.
@login_required
def view_order_history(request):

    # get all of the user's completed order and reference the the order id and date as a hyperlink.
    try:
        closed_orders = Order.objects.filter(buyer=request.user, date_complete__isnull=False)
        # if GET and they have products, display them
        if request.method == 'GET':
            template_name = 'orders/view_order_history.html'
            return render(request, template_name, {"closed_orders": closed_orders})


    except ObjectDoesNotExist:
        return HttpResponseRedirect('/no_order')
