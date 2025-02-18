import uuid
from django.db import models



class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=150, unique=True)
    image = models.ImageField(upload_to="brand_image")

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=225)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    display_image = models.ImageField(upload_to="product_display_images")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField() 
    uploaded_at = models.DateTimeField(auto_now_add=True)  

    class Meta:
        ordering = ["uploaded_at"]

    def __str__(self):
        return self.name
    


    
