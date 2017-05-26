from django.shortcuts import render

# invoked if there was no oder. it facilitates the display of a "no order" page.
def no_order(request):
  if request.method == 'GET':
    template_name = 'orders/no_order.html'
    return render(request, template_name)

