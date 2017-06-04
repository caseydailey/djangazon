# bring in the magic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

# import forms and models form this app
from website.models import UserOrder, LikeDislike, Product

@login_required
def recommendations(request):
    """
    purpose: Gives the user a list of recommended products based off categories from 
             from previous purchases.   

    author: Taylor Perkins, casey dailey

    args: request object

    returns: (render): a view of of the request, template populated with recommendations
    """
    
    if request.method == "GET":
        template_name = 'recommendations.html'            

        # get products user has liked or disliked
        likes_dislikes = LikeDislike.objects.filter(user=request.user)
        # print("Your likes_dislikes is a queryset:  {}".format(likes_dislikes))

        # get set of products user has purchased (puchase = liked)
        specific_products_purchased = ( UserOrder.objects.filter(order__buyer=request.user)
                                                         .exclude(order__date_complete__isnull=True)
                                                         .values('product')
                                                         .distinct())
        # print("Your specific_products_purchased is a queryset:  {}".format(specific_products_purchased))                                        

        # seperate likes and dislikes
        disliked_products = likes_dislikes.filter(liked=False).values('product')
        liked_products = likes_dislikes.filter(liked=True).values('product')        

        # union of puchased (one set of likes) and liked
        unique_set = specific_products_purchased.union(liked_products)

        # total distinct products liked        
        len_of_total_products_in_unique_set = len(unique_set)

        def create_category_percentage(product_set_length, len_of_overall):
            """
            purpose: determine a product categories relevance to a user by determining the percentage
                     of a given product category relative to their total likes/purchases
            author: taylor perkins, casey dailey
            args: product_set_length: (integer) number of products in a given category
                  len_of_overall: (integer) number of products liked/purchased
            returns: (list) where list[0] is a boolean indicating whether the product category represents 25%
                      or more of the user's total likes/purchases and list[1] is the actual percentage
            """
            percentage = product_set_length / len_of_overall * 100
            if percentage >= 25:
                return [True, percentage]
            else:
                return [False, percentage]

        
        # make a dict like this: 
        # 'electronics': {'products': {<Product: JBL Speakers>, <Product: Mac Book Pro 13>, <Product: Iphone 6s>}}, 
        # 'home': {'products': {<Product: Dining Table>, <Product: Knife Set>}}, 
        # 'general': {'products': {<Product: Yummy potato chips>, <Product: chop sticks>}}, 
        # 'clothing': {'products': {<Product: Diesel Jeans>}}, 
        # 'sports': {'products': {<Product: Vollyball>}}
        # 
        # where the keys are the category names
        # and the values are dictionaries
        # with a key 'products' whose values 
        # are sets of products in those categories
        # the user has either like or purchased
        category_dict = dict()
        for product in unique_set:            
            django_product = Product.objects.get(pk=product['product'])
            category_name = django_product.product_category.category_name            
            try: 
                category_dict[category_name]['products'].add(django_product)
            except KeyError:
                category_dict[category_name] = dict()         
                category_dict[category_name]['products'] = set()
                category_dict[category_name]['products'].add(django_product)

        print("category_dict: {}".format(category_dict))

        
        # update category_dict's values (themselves product_dicts) 
        # to have a new key 'percentage' whose value represents
        #  whether and how relevant products from a given category are
        #  
        #  example category_dict:
        #   
        # 'electronics': {'products': {<Product: JBL Speakers>, <Product: Mac Book Pro 13>, <Product: Iphone 6s>}, 
        #                 'percentage': [True, 33.33333333333333]}, 
        # 'home': {'products': {<Product: Dining Table>, <Product: Knife Set>}, 
        #          'percentage': [False, 22.22222222222222]}, 
        # 'general': {'products': {<Product: Yummy potato chips>, <Product: chop sticks>}, 
        #             'percentage': [False, 22.22222222222222]}, 
        # 'clothing': {'products': {<Product: Diesel Jeans>}, 
        #              'percentage': [False, 11.11111111111111]}, 
        # 'sports': {'products': {<Product: Vollyball>}, 
        #            'percentage': [False, 11.11111111111111]}}
        pure_category_dict = dict()
        for key, value in category_dict.items():
            len_of_products_set = len(value['products'])
            percentage_list = create_category_percentage(len_of_products_set, 
                                                         len_of_total_products_in_unique_set)
            category_dict[key]['percentage'] = percentage_list

            # if the category is relevant (represents more than 25% of likes/purchases)
            # assign that category name as a key and the value of that key as 
            # a dictionary of products and that categories relevance
            # 
            # like this: 
            # 'electronics': {'products': {<Product: JBL Speakers>, <Product: Mac Book Pro 13>, <Product: Iphone 6s>}, 
            #                 'percentage': [True, 33.33333333333333]}}
            if percentage_list[0]:
                pure_category_dict[key] = category_dict[key]


        print("category_dict: {}".format(category_dict))
        print("\n\nYour pure category list: {}\n\n".format(pure_category_dict))
        print("pure_category_dict: {}".format(pure_category_dict))

        # eliminate products purchase, liked, or disliked form search
        products_not_to_search_for = (liked_products.union(disliked_products
                                                    .union(specific_products_purchased)))
        # print(products_not_to_search_for)
        
        # get what products are left
        remaining_products = (Product.objects
                                     .filter(product_category__category_name__in=pure_category_dict.keys())
                                     .exclude(pk__in=products_not_to_search_for))
        # print(remaining_products)

        # products_not_liked_or_bought = Product.objects.all().exclude(pk__in=[x for x in unique_set])

        # get the user's open orders
        open_orders = UserOrder.objects.filter(order__buyer=request.user, order__payment_type__isnull=True)
        # print(open_orders)

        return render(request, template_name, {
            'likes_dislikes': likes_dislikes,
            'specific_products_purchased': specific_products_purchased, 
            'disliked_products': disliked_products,
            'liked_products': liked_products,
            'unique_set': unique_set,
            'remaining_products': remaining_products,
            'open_orders': open_orders})
