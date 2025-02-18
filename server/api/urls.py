from django.urls import path
from .views import main, products, get_products, create_products, delete_products, update_products, BrandCreateListView, BrandDetailView


urlpatterns = [
    path('', main, name='products'),
    path('product/', products, name='All products'),
    path('product/<uuid:id>', get_products, name='product'),
    path('product/create', create_products, name= 'createproduct'),
    path('product/delete/<uuid:id>', delete_products, name= 'deleteproduct'),
    path('product/update/<uuid:id>', update_products, name= 'updateproduct'),
    path('brand', BrandCreateListView.as_view(), name='create and get all endpoint'),
    path('brand/<uuid:pk>', BrandDetailView.as_view(), name='Get brand by ID endpoint'), # Retrieve a special Brand by ID



]