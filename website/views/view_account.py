from django.shortcuts import render
from website.forms import UserForm, ProfileForm

def view_account(request):

    if request.method == 'GET':

        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    
        return render(request, "account/view_account.html", {
            "user_form": user_form,
            "profile_form": profile_form,
            })

    elif request.method == 'POST':   

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()    
            profile_form = profile_form.save(commit=False)
            profile_form.user = request.user
            profile_form.save()

            return HttpResponseRedirect("view_account")

        else:

            return render (request, "account/view_account.html", {
                "user_form": user_form,
                "profile_form": profile_form,
                })
            
