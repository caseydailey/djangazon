from django.conf.urls import url
import website.views 

app_name = "website"
urlpatterns = [
    url(r'^$', website.views.index, name='index'),
    url(r'^add_payment_type$', website.views.add_payment_type, name='add_payment_type'),
    url(r'^display_order/(?P<order_id>[0-9]+)$', website.views.display_order, name='display_order'),
    url(r'^edit_payment_type$', website.views.edit_payment_type, name='edit_payment_type'),
    url(r'^edit_user_account$', website.views.edit_account, name='edit_account'),
    url(r'^list_products$', website.views.list_products, name='list_products'),
    url(r'^login$', website.views.login_user, name='login'),
    url(r'^logout$', website.views.user_logout, name='logout'),
    url(r'^my_products$', website.views.my_products, name='my_products'),
    url(r'^notifications$', website.views.notifications, name='notifications'),
    url(r'^no_order$', website.views.no_order, name='no_order'),
    url(r'^no_payment_type$', website.views.no_payment_type, name='no_payment_type'),
    url(r'^no_products$', website.views.no_products, name='no_products'),
    url(r'^order_complete/(?P<order_id>[0-9]+)$', website.views.order_complete, name='order_complete'),
    url(r'^product_category/(?P<category_id>[0-9]+)$', website.views.view_specific_product, name='product_category_view'),
    url(r'^product_categories$', website.views.product_categories, name='product_categories_view'),
    url(r'^product_details/(?P<product_id>[0-9]+)/$', website.views.product_details, name='product_details'),
    url(r'^recommendations$', website.views.recommendations, name='recommendations'),
    url(r'^register$', website.views.register, name='register'),
    url(r'^recommend_product/(?P<product_id>[0-9]+)/$', website.views.recommend_product, name='recommend_product'),
    url(r'^sell_product$', website.views.sell_product, name='sell'),
    url(r'^view_account$', website.views.view_account, name='view_account'),
    url(r'^view_checkout/(?P<order_id>[0-9]+)$', website.views.view_checkout, name='view_checkout'),
    url(r'^view_order$', website.views.view_order, name='view_order'),
    url(r'^view_order_history$', website.views.view_order_history, name="view_order_history"),
]
