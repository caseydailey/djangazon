from django.shortcuts import render
from django.db.models import Q

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
        print("search: {}".format(search_query))
        # if they're searching and search_query is truthy (meaning it's not blank),
        # filter products where title, description, or city contains search_query
        if 'search_box' in request.GET and search_query:
            results = set()
            results = Product.objects.filter(Q(title__contains=search_query) | Q(description__contains=search_query) | Q(city__contains=search_query)).exclude(quantity=0)            

            # if any return match, display
            if results:
                return render(request, 'product/list.html', {"results": results})

            # no results
            else:
                return render(request, 'product/no_products.html')

        # they searched for nothing
        else:
            return render(request, 'product/no_products.html')
