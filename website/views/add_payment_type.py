# bring in the magic
from django.http import HttpResponseRedirect
from django.shortcuts import render

# import forms and models form this app
from website.forms import AddPaymentForm
from website.models import PaymentType

def add_payment_type(request):
    """
    purpose: Allows user to add a payment type to their account, from a submenu in the acount information view

    author: Harry Epstein

    args: name: (string), acount number of credit card

    returns: (render): a view of of the request, template to use, and product obj
    """
    # if GET, create a payment form based on our model and render that form. 
    if request.method == 'GET':
        add_payment_form = AddPaymentForm()
        template_name = 'account/add_payment.html'
        return render(request, template_name, {'add_payment_form': add_payment_form})

    # if POST, gather form_data, save, and redirect to account view.
    elif request.method == 'POST':
        form_data = request.POST

        p = PaymentType(
            user=request.user,
            name=form_data['name'],
            account_number=form_data['account_number'])

        p.save()
        template_name = 'account/add_payment.html'
        return HttpResponseRedirect('/view_account')
