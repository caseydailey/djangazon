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

        user_products = Product.objects.filter(seller=request.user)    

        print(user_products)

        if user_products:
            num_of_products_sold = dict()
            for product in user_products:
                num_of_products_sold[product.title] = UserOrder.objects.filter(product=product).exclude(order__in=[x for x in Order.objects.filter(payment_type=None)]).count()


            ratings_set = Ratings.objects.filter(product=product.id)
            average_rating_for_products = dict()
            for product in ratings_set:
                product_name = str(product)
                if product_name in average_rating_for_products:
                    pass
                else:
                    average_rating = ratings_set.values('rating').aggregate(average_rating=Avg('rating'))
                    average_rating_for_products[product_name] = average_rating['average_rating']

            print("average_rating_for_products: {}".format(average_rating_for_products))

            return render(request, template_name, {
                "user_products": user_products,
                "num_of_products_sold": num_of_products_sold,
                "average_rating_for_products": average_rating_for_products})
        else:
            return render(request, "product/no_products_for_sale.html")
