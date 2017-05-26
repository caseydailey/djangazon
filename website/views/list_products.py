from django.shortcuts import render

def list_products(request):
  if request.method == 'GET':
    template_name = 'product/list.html'
    return render(request, template_name)
