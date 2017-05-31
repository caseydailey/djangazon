from django.conf.urls import url
from website.views import (
                        add_payment_type, 
                        edit_account, 
                        edit_payment_type, 
                        index, 
                        list_products, 
                        login_user, 
                        my_products,
                        notifications,
                        no_order, 
                        no_payment_type, 
                        no_products,
                        order_complete, 
                        product_categories, 
                        product_details, 
                        recommend_product,
                        register, 
                        sell_product, 
                        user_logout, 
                        view_account,
                        view_order, view_checkout, 
                        view_specific_product)

app_name = "website"
urlpatterns = [
    url(r'^$', index.index, name='index'),
    url(r'^add_payment_type$', add_payment_type.add_payment_type, name='add_payment_type'),
    url(r'^edit_payment_type$', edit_payment_type.edit_payment_type, name='edit_payment_type'),
    url(r'^edit_user_account$', edit_account.edit_account, name='edit_account'),
    url(r'^list_products$', list_products.list_products, name='list_products'),
    url(r'^login$', login_user.login_user, name='login'),
    url(r'^logout$', user_logout.user_logout, name='logout'),
    url(r'^my_products$', my_products.my_products, name='my_products'),
    url(r'^notifications$', notifications.notifications, name='notifications'),
    url(r'^no_order$', no_order.no_order, name='no_order'),
    url(r'^no_payment_type$', no_payment_type.no_payment_type, name='no_payment_type'),
    url(r'^no_products$', no_products.no_products, name='no_products'),
    url(r'^order_complete/(?P<order_id>[0-9]+)$', order_complete.order_complete, name='order_complete'),
    url(r'^product_category/(?P<category_id>[0-9]+)$', view_specific_product.view_specific_product, name='product_category_view'),
    url(r'^product_categories$', product_categories.product_categories, name='product_categories_view'),
    url(r'^product_details/(?P<product_id>[0-9]+)/$', product_details.product_details, name='product_details'),
    url(r'^register$', register.register, name='register'),
    url(r'^recommend_product/(?P<product_id>[0-9]+)/$', recommend_product.recommend_product, name='recommend_product'),
    url(r'^sell_product$', sell_product.sell_product, name='sell'),
    url(r'^view_account$', view_account.view_account, name='view_account'),
    url(r'^view_checkout/(?P<order_id>[0-9]+)$', view_checkout.view_checkout, name='view_checkout'),
    url(r'^view_order$', view_order.view_order, name='view_order')
]


