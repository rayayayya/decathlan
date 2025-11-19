from django.urls import path
from main.views import (
    show_main, 
    create_product_ajax,
    edit_product_ajax,
    delete_product_ajax,
    show_products,
    show_xml,
    show_json,
    show_xml_by_id,
    show_json_by_id,
    register,
    login_user,
    logout_user,
    proxy_image,
    create_product_flutter,
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-ajax/', create_product_ajax, name='create_product_ajax'),
    path('edit-product-ajax/<str:id>/', edit_product_ajax, name='edit_product_ajax'),
    path('delete-product-ajax/<str:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('product/<str:id>/', show_products, name='product_detail'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),

]
