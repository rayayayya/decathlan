from django.urls import path
from main.views import (
    show_main, 
    create_product_ajax,
    edit_product_ajax,
    delete_product_ajax,
    get_product_json,
    show_products,
    show_xml,
    show_json,
    show_xml_by_id,
    show_json_by_id,
    register,
    login_user,
    logout_user
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),

    # AJAX endpoints
    path('create-product-ajax/', create_product_ajax, name='create_product_ajax'),
    path('edit-product-ajax/<str:id>/', edit_product_ajax, name='edit_product_ajax'),
    path('delete-product-ajax/<str:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('get-product-json/<str:id>/', get_product_json, name='get_product_json'),

    # Product detail
    path('product/<str:id>/', show_products, name='product_detail'),

    # JSON/XML
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),

    # Auth
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
