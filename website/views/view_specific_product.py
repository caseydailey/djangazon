# bring in the magic
from django.shortcuts import get_object_or_404, render

# import forms and models form this app
from website.models import Product, Category

def view_specific_product(request, category_id):
    """
    purpose: Allows user to view a specific category view, which contains all products directly related to the given category

        For an example, visit /product_category/1 to see a view on the first category created
        dispaying all products related. All products also have links sending you directly to their specific page

    author: Taylor Perkins

    args: category_id: (integer): id of category we are viewing

    returns: (render): a view of of the request, template to use, and product obj
                (category): category we are viewing
                (products): all products related to given category
    """
    # get the categories and display them
    template_name = 'product/category.html'
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(product_category=category).exclude(quantity=0)

    # display products
    return render(request, template_name, {
        "category": category,
        "products": products})
