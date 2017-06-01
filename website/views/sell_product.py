# bring in the magic
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

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
        file_data = request.FILES
        print(file_data)

        def create_product(product_delivery, product_image):
            p = Product(
                seller=request.user,
                title=form_data['title'],
                description=form_data['description'],
                price=form_data['price'],
                quantity=form_data['quantity'],
                local_delivery=product_delivery,
                city=form_data['city'],
                image_path=product_image,

                # create an instance of category of where category_name = the user's choice
                product_category=Category.objects.get(category_name=form_data['product_category']))
            p.save()
            return p

        product_delivery = None
        product_image = None

        if 'image_path' in request.FILES:
            print("heyHERE")
            product_image = request.FILES['image_path']
        else:
            print("heyElse")
            product_image = None

        try:

            if 'local_delivery' in request.POST:
                product_delivery = True
                product = create_product(product_delivery, product_image)
                return HttpResponseRedirect('product_details/{}'.format(product.id))
        except MultiValueDictKeyError:
            product_delivery = False
            product = create_product(product_delivery, product_image)
            return HttpResponseRedirect('product_details/{}'.format(product.id))
