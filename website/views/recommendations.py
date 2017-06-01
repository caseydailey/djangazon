# bring in the magic
from django.shortcuts import render

# import forms and models form this app

def recommendations(request):
    """
    purpose: Allows user to view product_detail view, which contains a very specific view
        for a singular product

        if the user clicks "add to order". Their current open order will be updated and the
        user will be routed to that order.

        For an example, visit /product_details/1/ to see a view on the first product created
        displaying title, description, quantity, price/unit, and "Add to order" button

    author: Taylor Perkins, Justin Short

    args: product_id: (integer): id of product we are viewing

    returns: (render): a view of of the request, template to use, and product obj
    """
    # If trying to view, render product corresponding to id passed    
    if request.method == "GET":
        template_name = 'recommendations.html'    
        return render(request, template_name, {})
