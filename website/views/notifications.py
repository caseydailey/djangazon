# bring in the magic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# import forms and models form this app


@login_required
def notifications(request):
    """
    purpose: display a user's order and handle actions handle checkout (apply a payment type)

    args: request, order_id (integer): the particular order being viewed

    returns: render display of products and payment types associated with a user and various redirects
    """
    if request.method == 'GET':
        template_name = 'notifications.html'
        return render(request, template_name)
