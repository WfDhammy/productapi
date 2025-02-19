from django.http import Http404
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Product, Brand, Category
from .serializers import ProductSerializer, BrandSerializer, CategorySerializer

from rest_framework.views import APIView

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
    lookup_field = 'id'


class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CategorySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CategorySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)