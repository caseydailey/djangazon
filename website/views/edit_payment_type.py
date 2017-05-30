# bring in the magic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# import forms and models form this app
from website.models import PaymentType, Profile

@login_required
def edit_payment_type(request):
    """
    purpose: expose user's payment types and provide affordance to delete

    author: casey dailey

    args: request

    returns: rendered view of user's payment types if there are any; redirect if none
    """
    payment_types = PaymentType.objects.filter(user=request.user)

    # if GET and there are payment types, display them.
    if request.method == "GET" and payment_types:
        template_name = 'account/edit_payment.html'        
        my_user = Profile.objects.get(user=request.user)    
        return render(request, template_name, {
            "payment_types": payment_types,
            "my_user": my_user})

    # if POST and it was the 'delete' get the particular payment type and delete it.
    # if that was the last one, redirect to no_payment_type.html, else render remaining payment types
    elif request.method == 'POST':
        if 'payment_type' in request.POST:
            payment_type = PaymentType.objects.get(pk=request.POST.get('payment_type'))
            payment_type.delete()
            if payment_types:
                return render(request, template_name, {
                    "payment_types": payment_types})

            elif not payment_types:
                return HttpResponseRedirect('/no_payment_type') 

    # if atttempting to view, but have no payment types, redirect to no_payment_type
    elif request.method == "GET" and not payment_types:
        print("NO PAYMENT TYPES")
        return HttpResponseRedirect('/no_payment_type')
