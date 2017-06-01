from django.shortcuts import render

def view_account(request):
    template_name = 'account/view_account.html'
    if request.method == 'GET':
        return render(request, template_name)

    if request.method == "POST":
        return render(request, template_name) 
            
