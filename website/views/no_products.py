from django.shortcuts import render

# invoked if no payment available. it facilitates the display of no_products page.
def no_products(request):
  if request.method == 'GET':
    template_name = 'product/no_products.html'
    return render(request, template_name)
