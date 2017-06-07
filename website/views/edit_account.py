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

        # create form instances, prepopulated with user info
        user_form = EditUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    
        # render pre-populated forms

        return render(request, "account/edit_account.html", {
            "user_form": user_form,
            "profile_form": profile_form})

    # if submitting edited form info
    elif request.method == 'POST':

        # instantiate forms
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile) 

        if user_form.is_valid() and profile_form.is_valid():

            # forms are valid. get their data and save
            user_form.save()    
            profile_form = profile_form.save(commit=False)
            profile_form.user = request.user
            profile_form.save()

            return HttpResponseRedirect("view_account")

        # input not valid. render editable forms.
        else:
            return render (request, "account/edit_account.html", {
                "user_form": user_form,
                "profile_form": profile_form,
                })

