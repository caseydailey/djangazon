from django.shortcuts import render

def view_account(request):
    if request.method == 'GET':
        template_name = 'account/view_account.html'
        return render(request, template_name)
            
