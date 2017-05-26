from django.conf.urls import url

from website.views import index
# from . import views

app_name = "website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^sell_product$', views.sell_product, name='sell'),
    url(r'^list_products$', views.list_products, name='list_products'),
    url(r'^product_category/(?P<category_id>[0-9]+)$', views.view_specific_product, name='product_category_view'),
    url(r'^product_categories$', views.product_categories, name='product_categories_view'),
    url(r'^product_details/(?P<product_id>[0-9]+)/$', views.product_details, name='product_details'),
    url(r'^view_account$', views.view_account, name='view_account'),
    url(r'^edit_user_account$', views.edit_account, name='edit_account'),
    url(r'^edit_payment_type$', views.edit_payment_type, name='edit_payment_type'),
    url(r'^add_payment_type$', views.add_payment_type, name='add_payment_type'),
    url(r'^view_order$', views.view_order, name='view_order'),
    url(r'^view_checkout/(?P<order_id>[0-9]+)$', views.view_checkout, name='view_checkout'),
    url(r'^order_complete/(?P<order_id>[0-9]+)$', views.order_complete, name='order_complete'),
    url(r'^no_order$', views.no_order, name='no_order'),
    url(r'^no_payment_type$', views.no_payment_type, name='no_payment_type')

]
