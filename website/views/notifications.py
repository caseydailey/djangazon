# bring in the magic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect

from website.processors import navbar_notifications
from website.models import Recommendations

@login_required
def notifications(request):
    """
    purpose: display a user's order and handle actions handle checkout (apply a payment type)

    args: request, order_id (integer): the particular order being viewed

    returns: render display of products and payment types associated with a user and various redirects

    author: Taylor Perkins
    """
    template_name = 'notifications.html'
    product_recommendations = navbar_notifications(request)
    if request.method == 'GET':

        return render(request, template_name, {
                'product_recommendations': product_recommendations['notifications']})

    if request.method == 'POST':           

        # if user is viewing their notifications, show them and mark as viewed
        # so the count and view can be adjusted.
        if 'go_to_recommendation' in request.POST:                       
            recommendation_post = request.POST.get('go_to_recommendation')
            recommendation = Recommendations.objects.get(pk=recommendation_post)            
            recommendation.viewed = True
            recommendation.save()
            return HttpResponseRedirect('/product_details/{}'.format(recommendation.product.id))            

        return render(request, template_name)











