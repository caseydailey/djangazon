from django.shortcuts import render
from website.models import Product, UserOrder, Order, Ratings
from django.db.models import Avg

def my_products(request):
    """
    purpose: display information related to a user's product sales

    author: taylor perkins, casey dailey

    args: request

    returns: rendered view of product sales info
    """
    if request.method == 'GET':
        template_name = 'product/my_products.html'

        # get products the user's have sold 
        user_products = Product.objects.filter(seller=request.user)

        # if user has sold products
        # build a dict like this:
        # product_name: number sold
        # product_name: number sold
        if user_products:
            num_of_products_sold = dict()
            average_rating_for_products = dict()
            for product in user_products:
                num_of_products_sold[product.title] = UserOrder.objects.filter(product=product).exclude(order__in=[x for x in Order.objects.filter(payment_type=None)]).count()

                # get productg ratings
                ratings_set = Ratings.objects.filter(product=product.id)
                # build a dict like this:
                # product_name: average rating
                # product_name: average rating
                for product in ratings_set:
                    product_name = str(product)
                               
                    if product_name in average_rating_for_products:
                        pass
                    else:
                        average_rating = ratings_set.values('rating').aggregate(average_rating=Avg('rating'))
                        average_rating_for_products[product_name] = average_rating['average_rating']            

                return render(request, template_name, {
                    "user_products": user_products,
                    "num_of_products_sold": num_of_products_sold,
                    "average_rating_for_products": average_rating_for_products})

        else:
            return render(request, "product/no_products_for_sale.html")

    # user is trying to remove a product for sale   
    if request.method == 'POST':
        user_products = Product.objects.filter(seller=request.user)

        if 'delete_product' in request.POST:

            # Get all completed orders
            # get the target product and set it's quantity to 0.
            # this is effectively a "soft delete", no longer available, but still in the database.
            all_complete_orders = UserOrder.objects.all().exclude(order__date_complete__isnull=False)
            target_product = request.POST.get('product')
            product = Product.objects.get(pk=target_product)
            product.quantity = 0
            product.save()

            return render(request, "product/no_products_for_sale.html")
