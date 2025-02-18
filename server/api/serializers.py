from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'display_image', 'price', 'quantity', 'uploaded_at']
        read_only_fields = ['id','uploaded_at']


