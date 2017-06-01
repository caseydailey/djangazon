from website.models import Recommendations


def navbar_notifications(request):
    # A context processor that provides 'app', 'user' and 'ip_address'.                     
    if request.user.is_authenticated():        
        notifications = Recommendations.objects.filter(to_person=request.user).exclude(viewed=True)
        return {
            'app': 'My app',                
            'ip_address': request.META['REMOTE_ADDR'],
            'notifications': notifications}

    return {'notifications': 0}


