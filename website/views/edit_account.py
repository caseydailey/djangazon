from django.shortcuts import render

def edit_account(request):
  if request.method == 'GET':
    template_name = 'account/edit_account.html'
    return render(request, template_name)
