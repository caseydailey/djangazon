from django.shortcuts import render

# invoked if no payment available. it facilitates the display of no_payment_type page.
def no_payment_type(request):
  if request.method == 'GET':
    template_name = 'account/no_payment_type.html'
    return render(request, template_name)
