# bring in the magic
from django.shortcuts import render
from website.models import Product

# display the index template
def index(request):
  '''
  purpose: Shows last 20 products that have been added to the database

  author: miriam rozenbuam

  args: request

  returns: (render): a view of the request, template to use, and product obj
  ''' 
  template_name = 'index.html'  
  newest_20_products = Product.objects.all().order_by("-id")[:20]
  return render(request, template_name, {
        'newest_20_products': newest_20_products})
