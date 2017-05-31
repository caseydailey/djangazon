from website.models import Recommendations


def navbar_notifications(request):
    # A context processor that provides 'app', 'user' and 'ip_address'.                 
    print(request.user.is_authenticated())
    if request.user.is_authenticated():
        print("I am here")
        notifications = Recommendations.objects.filter(to_person=request.user).exclude(viewed=True).count()
        return {
            'app': 'My app',                
            'ip_address': request.META['REMOTE_ADDR'],
            'notifications': notifications}

    return {'notifications': 0}


