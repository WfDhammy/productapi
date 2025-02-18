from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Product, Brand, Category
from .serializers import ProductSerializer, BrandSerializer, CategoeySerializer

# Create your views here.
@api_view()
def main(request):
    return Response({"message": "Hello, World!", "status": status.HTTP_200_OK })

@api_view()
def products(request):
    obj = Product.objects.all()
    serializer = ProductSerializer(obj, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view()
def get_products(request, id):
    obj = get_object_or_404(Product, id=id)
    serializer = ProductSerializer(obj)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def create_products(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def delete_products(request, id):
    obj = get_object_or_404(Product, id=id)
    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def update_products(request, id):
    obj = get_object_or_404(Product, id=id)
    serializer = ProductSerializer(obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandCreateListView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer