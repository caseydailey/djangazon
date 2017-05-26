# bring in the magic
from django.http import HttpResponseRedirect
from django.shortcuts import render

# import forms and models form this app
from website.forms import ProductForm
from website.models import Product, Category

def sell_product(request):
    """
    purpose: produce a form for the user to create a product to sell

    author: casey dailey

    args: request

    returns: redirect to detail view for product created
    """
    # if attempting to view, render the form.
    if request.method == 'GET':
        product_form = ProductForm()
        template_name = 'product/create.html'
        return render(request, template_name, {'product_form': product_form})

    # if POST, gather form data and save, then redirect to details for that product
    elif request.method == 'POST':
        form_data = request.POST

        p = Product(
            seller=request.user, 
            title=form_data['title'], 
            description=form_data['description'], 
            price=form_data['price'], 
            quantity=form_data['quantity'], 

            # create an instance of category of where category_name = the user's choice
            product_category=Category.objects.get(category_name=form_data['product_category']))

        p.save()
        return HttpResponseRedirect('product_details/{}'.format(p.id))
