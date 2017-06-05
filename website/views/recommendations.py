# bring in the magic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# import forms and models
from website.models import UserOrder, LikeDislike, Product

@login_required
def recommendations(request):
    """
    purpose: Gives the user a list of recommended products  

    author: Taylor Perkins, casey dailey

    args: the django request object 

    returns: rendered template populated with recommendations
    """
    
    if request.method == "GET":
        template_name = 'recommendations.html'            

        # get likes and dislikes
        likes_and_dislikes = LikeDislike.objects.filter(user=request.user)
        likes = likes_and_dislikes.filter(liked=True).values('product')        
        dislikes = likes_and_dislikes.filter(liked=False).values('product')

        # get products user has purchased (puchase = liked)
        purchased = ( UserOrder.objects.filter(order__buyer=request.user)
                                                         .exclude(order__date_complete__isnull=True)
                                                         .values('product')
                                                         .distinct())
        # union of puchased and liked
        liked_or_purchased = purchased.union(likes)

        # total distinct products liked        
        count_liked_or_purchased = len(liked_or_purchased)

        def cat_is_relevant(prods_in_cat, total_liked_prods):
            """
            purpose: determine category's relevance to a user by determining the percentage
                     of a given product category relative to their total likes/purchases
            
            author: taylor perkins, casey dailey
            
            args: prods_in_cat: (integer) number of products puchased or liked in a given category
                  total_liked_prods: (integer) number of products liked/purchased
            
            returns: Boolean indicating whether category is relevant
            """
            relevance = prods_in_cat / total_liked_prods

            if relevance >= .25:
                return True
            else:
                return False

        
        # make a dict like this: 
        # 
        # 'electronics': {'products': {<Product: JBL Speakers>, <Product: Mac Book Pro 13>, <Product: Iphone 6s>}}, 
        # 'home': {'products': {<Product: Dining Table>, <Product: Knife Set>}}, 
        # 'general': {'products': {<Product: Yummy potato chips>, <Product: chop sticks>}}, 
        # 'clothing': {'products': {<Product: Diesel Jeans>}}, 
        # 'sports': {'products': {<Product: Vollyball>}}
        # 
        # the keys are the category names
        # the values are dicts
        # whose key 'products' have values which
        # are sets of products in those categories
        # the user has either like or purchased
        category_dict = dict()
        for product in liked_or_purchased:            
            prod_name = Product.objects.get(pk=product['product'])
            category_name = prod_name.product_category.category_name            
            try: 
                category_dict[category_name]['products'].add(prod_name)
            except KeyError:
                category_dict[category_name] = dict()         
                category_dict[category_name]['products'] = set()
                category_dict[category_name]['products'].add(prod_name)
        
        # update category_dict like this:
        # 
        # 'electronics': True, 
        # 'home': False, 
        # 'general': False, 
        # 'clothing': False, 
        # 'sports': False
        #
        # True means relevant 
        # relevant means the amount of products liked or purchased in that category
        # represent at least 25% of the total products purchased or liked by that user
        # 
        # append relevant categories to a list of relevant categories
        # ex:
        # relevant_categories: ['electronics'] 
        relevant_categories = list()
        for category in category_dict:
            num_prods_in_cat = len(category_dict[category]['products'])
            is_relevant = cat_is_relevant(num_prods_in_cat, count_liked_or_purchased)
            category_dict[category] = is_relevant

            if is_relevant:
                relevant_categories.append(category)

        # print("category_dict: {}".format(category_dict))
        # print("relevant_categories: {}\n\n".format(relevant_categories))

        # get products purchased, liked, or disliked
        liked_disliked_purchased = (likes.union(dislikes.union(purchased)))
        
        # recommend products form relevant_categories
        # that have not been purchased, liked, or disliked
        recommended_products = (Product.objects
                                       .filter(product_category__category_name__in=relevant_categories)
                                       .exclude(pk__in=liked_disliked_purchased))

        # get the user's open orders. why?
        open_orders = UserOrder.objects.filter(
                                                order__buyer=request.user, 
                                                order__payment_type__isnull=True)

        return render(request, template_name, {
            'likes_and_dislikes': likes_and_dislikes, 
            'recommended_products': recommended_products,
            'open_orders': open_orders})
