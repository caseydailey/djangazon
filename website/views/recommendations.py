# bring in the magic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

# import forms and models form this app
from website.models import UserOrder, LikeDislike, Product

@login_required
def recommendations(request):
    """
    purpose: Gives the user a list of recommended products based off of user categories from 
    from previous purchases.   

    author: Taylor Perkins

    args: None

    returns: (render): a view of of the request, template to use
    """
    # If trying to view, render product corresponding to id passed    
    if request.method == "GET":
        template_name = 'recommendations.html'            

        likes_dislikes = LikeDislike.objects.filter(user=request.user)
        print("Your likes_dislikes is a queryset:  {}".format(likes_dislikes))

        specific_products_purchased = UserOrder.objects.filter(order__buyer=request.user).exclude(order__date_complete__isnull=True).values('product').distinct()
        print("Your specific_products_purchased is a queryset:  {}".format(specific_products_purchased))                                

        disliked_products = likes_dislikes.filter(liked=False).values('product')
        liked_products = likes_dislikes.filter(liked=True).values('product')        

        unique_set = specific_products_purchased.union(liked_products)        
        len_of_total_products_in_unique_set = len(unique_set)

        def create_category_percentage(product_set_length, len_of_overall):
            percentage = product_set_length / len_of_overall * 100
            if percentage >= 25:
                return [True, percentage]
            else:
                return [False, percentage]

        category_dict = dict()
        for product in unique_set:            
            django_product = Product.objects.get(pk=product['product'])
            category_name = django_product.product_category.category_name            
            try: 
                category_dict[category_name]['products'].add(django_product)
            except KeyError:
                category_dict[category_name] = dict()         
                category_dict[category_name]['products'] = set()
                category_dict[category_name]['average'] = 0
                category_dict[category_name]['products'].add(django_product)

        print(category_dict)

        pure_category_list = dict()
        for key, value in category_dict.items():
            len_of_products_set = len(value['products'])
            print(len_of_products_set)
            print(len_of_total_products_in_unique_set)
            percentage_list = create_category_percentage(len_of_products_set, len_of_total_products_in_unique_set)
            category_dict[key]['percentage'] = percentage_list
            if percentage_list[0]:
                pure_category_list[key] = category_dict[key]

        print(category_dict)
        print("\n\nYour pure category list: {}\n\n".format(pure_category_list))
        # products_not_liked_or_bought = Product.objects.all().exclude(pk__in=[x for x in unique_set])

        return render(request, template_name, {
            'likes_dislikes': likes_dislikes,
            'specific_products_purchased': specific_products_purchased, 
            'disliked_products': disliked_products,
            'liked_products': liked_products,
            'unique_set': unique_set})
