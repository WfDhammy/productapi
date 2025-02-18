from django.urls import path
from .views import main, products, get_products, create_products, delete_products, update_products


urlpatterns = [
    path('', main, name='products'),
    path('product/', products, name='All products'),
    path('product/<uuid:id>', get_products, name='product'),
    path('product/create', create_products, name= 'createproduct'),
    path('product/delete', delete_products, name= 'deleteproduct'),
    path('product/update', update_products, name= 'updateproduct'),

]