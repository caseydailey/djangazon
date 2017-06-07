# bring in the magic
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

# import forms and models form this app
from website.models import Product, Order, UserOrder, LikeDislike

def product_details(request, product_id):
    """
    purpose: Allows user to view product_detail view, which contains a very specific view
        for a singular product

        if the user clicks "add to order". Their current open order will be updated and the
        user will be routed to that order.

        For an example, visit /product_details/1/ to see a view on the first product created
        displaying title, description, quantity, price/unit, and "Add to order" button

    author: Taylor Perkins, Justin Short

    args: product_id: (integer): id of product we are viewing

    returns: (render): a view of of the request, template to use, and product obj
    """
    
    # If trying to view, render product corresponding to id passed
    product = get_object_or_404(Product, pk=product_id)


    if request.method == "GET":
        template_name = 'product/details.html'
        try:
            if request.user.is_authenticated():            
                product_liked = LikeDislike.objects.get(product=product, user=request.user)
            else:
                product_liked = None             

        except ObjectDoesNotExist:
            product_liked = None        

    # if trying to to buy, get the user's orders
    elif request.method == "POST":
        def create_like_dislike_instance(bool):
            liked_instance = LikeDislike(
                user=request.user,
                product=Product.objects.get(pk=product_id),
                liked=bool)
            liked_instance.save()
            return liked_instance

        print(request.user.is_authenticated())                
        try:
            product_liked = LikeDislike.objects.get(product=product, user=request.user)
            if product_liked:
                return HttpResponseRedirect('/product_details/{}'.format(product_id))
        except MultipleObjectsReturned:
            return HttpResponseRedirect('/product_details/{}'.format(product_id))
        except ObjectDoesNotExist:
            pass

        if 'like_dislike' in request.POST:
            print(request.POST.get('like_dislike'))                        
            if request.POST.get('like_dislike') == 'Like':
                create_like_dislike_instance(True)
                return HttpResponseRedirect('/product_details/{}'.format(product_id))

            elif request.POST.get('like_dislike') == 'Dislike':
                create_like_dislike_instance(False)
                return HttpResponseRedirect('/product_details/{}'.format(product_id))            

        elif 'add_to_order' in request.POST:
            product = get_object_or_404(Product, pk=product_id)
            template_name = 'product/details.html'
            all_orders = Order.objects.filter(buyer=request.user)

            # try to get user's open order. assign the product to an order
            # we should look into the get_or_create method as a potential refactor
            try:
                open_order = all_orders.get(date_complete__isnull=True)
                user_order = UserOrder(
                    product=product,
                    order=open_order)
                user_order.save()

                return HttpResponseRedirect('/view_order')

            # if no open order, create one. and assign product to it. 
            except ObjectDoesNotExist:
                open_order = Order(
                    buyer=request.user,
                    payment_type=None,
                    date_complete=None)

                open_order.save()
                user_order = UserOrder(
                    product=product,
                    order=open_order)
                user_order.save()
                users_orders = Order.objects.filter(buyer=request.user)
                print(users_orders)

                return HttpResponseRedirect('/view_order')

    return render(request, template_name, {
        "product": product,
        "product_liked": product_liked})
