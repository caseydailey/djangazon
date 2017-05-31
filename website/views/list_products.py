from django.shortcuts import render
from website.models import Product

def list_products(request):
    """
    purpose: list products matching keyword in search

    author: casey dailey

    args: the full request object

    returns: rendered display of products matching keyword or city search
    """
    
    if request.method == 'GET':
        # get value of search_box
        search_query = request.GET.get('search_box')

        # if they're searching and search_query is truthy (meaning it's not blank), 
        # filter products where title, description, or city contains search_query
        if 'search_box' in request.GET and search_query:
            title_contains = Product.objects.filter(title__contains=search_query)
            description_contains = Product.objects.filter(description__contains=search_query)
            city_contains = Product.objects.filter(city__contains=search_query)

            # if any return match, display
            if title_contains or description_contains or city_contains:
                template_name = 'product/list.html'
                return render(request, template_name, {
                    "title_contains": title_contains, 
                    "description_contains": description_contains,
                    "city_contains": city_contains})

            # no results 
            else:
                template_name = 'product/no_products.html'
                return render(request, template_name)

    # they searched for nothing    
    else:
        template_name = 'product/no_products.html'
        return render(request, template_name)
