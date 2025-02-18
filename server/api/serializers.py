from rest_framework import serializers
from .models import Product, Category, Brand


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(slug_field='name', queryset=Brand.objects.all())
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'name', 'brand', '' 'description', 'display_image', 'price', 'quantity', 'uploaded_at']
        read_only_fields = ['id','uploaded_at']

class CategoeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        field = ['id', 'name', 'image']
        read_only_fields = ['id']
