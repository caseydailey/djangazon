from django.shortcuts import render

from website.models import Product, UserOrder, Order

def my_products(request):
    if request.method == 'GET':
        template_name = 'product/my_products.html'

        user_products = Product.objects.filter(seller=request.user)    

        print(user_products)

        num_of_products_sold = dict()
        for product in user_products:
            print("Here is your product: {}".format(product.title))
            num_of_products_sold[product.title] = UserOrder.objects.filter(product=product).exclude(order__in=[x for x in Order.objects.filter(payment_type=None)]).count()      

        print(num_of_products_sold)

        return render(request, template_name, {
            "user_products": user_products,
            "num_of_products_sold": num_of_products_sold})
