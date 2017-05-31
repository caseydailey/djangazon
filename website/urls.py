from django.conf.urls import url

from website.views import index, register, login_user, user_logout, sell_product, add_payment_type, product_categories, product_details, view_specific_product, edit_payment_type, view_order, view_checkout, list_products, view_account, edit_account, order_complete, no_order, no_payment_type, view_order_history, display_order

app_name = "website"
urlpatterns = [
    url(r'^$', index.index, name='index'),
    url(r'^register$', register.register, name='register'),
    url(r'^login$', login_user.login_user, name='login'),
    url(r'^logout$', user_logout.user_logout, name='logout'),
    url(r'^sell_product$', sell_product.sell_product, name='sell'),
    url(r'^list_products$', list_products.list_products, name='list_products'),
    url(r'^product_category/(?P<category_id>[0-9]+)$', view_specific_product.view_specific_product, name='product_category_view'),
    url(r'^product_categories$', product_categories.product_categories, name='product_categories_view'),
    url(r'^product_details/(?P<product_id>[0-9]+)/$', product_details.product_details, name='product_details'),
    url(r'^view_account$', view_account.view_account, name='view_account'),
    url(r'^edit_user_account$', edit_account.edit_account, name='edit_account'),
    url(r'^edit_payment_type$', edit_payment_type.edit_payment_type, name='edit_payment_type'),
    url(r'^add_payment_type$', add_payment_type.add_payment_type, name='add_payment_type'),
    url(r'^view_order$', view_order.view_order, name='view_order'),
    url(r'^view_order_history$', view_order_history.view_order_history, name="view_order_history"),
    url(r'^display_order/(?P<order_id>[0-9]+)$', display_order.display_order, name='display_order'),
    url(r'^view_checkout/(?P<order_id>[0-9]+)$', view_checkout.view_checkout, name='view_checkout'),
    url(r'^order_complete/(?P<order_id>[0-9]+)$', order_complete.order_complete, name='order_complete'),
    url(r'^no_order$', no_order.no_order, name='no_order'),
    url(r'^no_payment_type$', no_payment_type.no_payment_type, name='no_payment_type')
]
