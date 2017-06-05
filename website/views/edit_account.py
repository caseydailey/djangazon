from django.shortcuts import render
from website.forms import EditUserForm, ProfileForm
from django.http import HttpResponseRedirect

def edit_account(request):
    """
    author: miriam rozenbaum

    purpose: display a user's account details such as: first_name, last_name, address, phone. 
    args: request, user, profile

    returns: render display of current user logged in account details
    """
    if request.method == 'GET':

        user_form = EditUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

        return render(request, "account/edit_account.html", {
            "user_form": user_form,
            "profile_form": profile_form})

    elif request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)   
        print(user_form.is_valid())
        print(profile_form.is_valid())
        if user_form.is_valid() and profile_form.is_valid():
            print('if statement')
            user_form.save()    
            profile_form = profile_form.save(commit=False)
            profile_form.user = request.user
            profile_form.save()

            return HttpResponseRedirect("view_account")

        else:
            print('else statement')
            return render (request, "account/edit_account.html", {
                "user_form": user_form,
                "profile_form": profile_form,
                })

