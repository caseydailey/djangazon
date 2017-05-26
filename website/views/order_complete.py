from django.shortcuts import render

# this is invoke if when order is complete. it facilitates the display of a "success" page.
def order_complete(request, order_id):
  if request.method == 'GET':
    template_name = 'orders/order_complete.html'
    return render(request, template_name)
