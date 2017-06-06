# bring in the magic
from django.shortcuts import render

# import forms and models form this app
from website.models import Product, Category

def product_categories(request):
    """
    purpose: display all categories and the first few products in each

    author: Taylor Perkins, Justin Short

    args: request object
    """
    # get all the categories and products and initialize a dict
    all_categories = Category.objects.all()
    all_products = Product.objects.all().order_by('-id').exclude(quantity=0)
    top_three_per_cat = dict()

    # try to build a dict that looks like this:
    #  top_three_per_cat= {
    #   category_id : (product, product, product),
    #   category_id : (product, product, product),
    #   category_id : (product, product, product)
    #  }
    for product in all_products:
        try:
            cat_product = top_three_per_cat[product.product_category.id]
            if len(cat_product) < 3:
                cat_product.add(product)

        # if new category, set it's id as the key and initialize a set for it's value
        except KeyError:
            top_three_per_cat[product.product_category.id] = set()
            top_three_per_cat[product.product_category.id].add(product)
            print(top_three_per_cat)

    template_name = 'product/categories.html'
    return render(request, template_name, {'all_categories': all_categories, 
        'product': all_products, 
        'top_three_per_cat': top_three_per_cat})

