from django.shortcuts import render
from website.models import Product

def list_products(request):
  if request.method == 'GET':
    if 'search_box' in request.GET:
        search_query = request.GET.get('search_box')
        print("search_query: {}".format(search_query))
        title_contains = Product.objects.filter(title__contains=search_query)
        print("title_contains: {}".format(title_contains))
        description_contains = Product.objects.filter(description__contains=search_query)
        print("description_contains: {}".format(description_contains))
        city_contains = Product.objects.filter(city__contains=search_query)
        print("city_contains: {}".format(city_contains))

        template_name = 'product/list.html'
        return render(request, template_name, {
            "title_contains": title_contains, 
            "description_contains": description_contains,
            "city_contains": city_contains
            })
    else:
        template_name = 'product/list.html'
        return render(request, template_name)
