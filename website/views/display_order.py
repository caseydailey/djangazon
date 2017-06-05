from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F, FloatField, Sum
from website.models import Order, UserOrder, Product, Ratings

@login_required
def display_order(request, order_id):
    '''
      purpose: Show the selected order with it's products and the total price of the function.
               Also, handle the user's submissions of ratings for products

      author: Justin Short, casey dailey

      args: request, order_id

      returns: (render): a view of the request, template to use, and order oject
    '''
    # If trying to view, render product corresponding to id passed
    if request.method == "GET":

      # GET the users selected order
      target_order = Order.objects.get(pk=order_id)

      # Get the UserOrder for the user and selected object
      all_products = UserOrder.objects.all().filter(order=target_order)    
      product_ids = [p.product_id for p in all_products]
      
      # Calculate the sum of all products costs and assign to total
      total = all_products.aggregate(total_price=Sum('product__price'))

      template_name = 'orders/display_order.html'
      return render(request, template_name, {"target_order": target_order, 
                                               "all_products": all_products, 
                                               "total": total["total_price"],
                                               "product_ids": product_ids})
    # user is trying to submit a rating
    # get rating value and reference to product
    elif request.method == "POST":
      if "range" in request.POST:
        rating = request.POST.get('range')
        prod_id = request.POST.get('id')
        product = Product.objects.get(pk=prod_id)

        # check to see if product has been rated by this user
        try:
            rated_product = Ratings.objects.get(product=prod_id, 
                                            user=request.user.id)
            if rated_product:
                template_name = 'orders/already_rated.html'
                context = {"rating": rating,
                           "product": product}
                return render(request, template_name, context)

        # if product has not been rated by this user, rate it.
        except ObjectDoesNotExist:
                product_rating = Ratings(
                                        user=request.user,
                                        product=product,
                                        rating=rating)
                product_rating.save()
                template_name = 'orders/rate_success.html'
                context = {"rating": rating,
                           "product": product}
                return render(request, template_name, context)


