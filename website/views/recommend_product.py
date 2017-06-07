from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.models import User

from website.models import Product, Recommendations

def recommend_product(request, product_id):
    """
    purpose: Recommend a product to a friend

    author: Taylor Perkins

    args: the full request object

    returns: rendered display of products matching keyword or city search
    """

    # user is trying to recommend a product to another user, so:
    if request.method == 'GET':        
        template_name = 'product/recommend_product.html'
        product = Product.objects.get(pk=product_id)

        # get the value of the search box 
        search_query = request.GET.get('recommendation_search')

        # if they've actually entered something:
        if 'recommendation_search' in request.GET and search_query:            

            # to get the user whose name was input
            # and make a recommendation to that user
            # the recommendation will say who it's to, who it's from, which product,
            # and a boolean indicating whether the to_person has viewed it yet.
            try:
                to_user = User.objects.get(username=search_query)
                recommendations = Recommendations(
                    to_person=to_user,
                    from_person=request.user,
                    product=product,
                    viewed=False)
                recommendations.save()
                return HttpResponseRedirect('/product_details/{}'.format(product_id))

            # if the query returns no users:
            except ObjectDoesNotExist:                
                messages.info(request, "{} does not exist".format(search_query))
                return render(request, 'user_recommendation_fail.html', {
                    "product": product})

            return HttpResponseRedirect('/product_details/{}'.format(product_id))

        return render(request, template_name, {
            "product": product})




