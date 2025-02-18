import uuid
from django.db import models



class Product(models.Model):
    id = models.AutoField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=225)
    description = models.TextField()
    display_image = models.ImageField(upload_to="product_display_images")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField() 
    uploaded_at = models.DateTimeField(auto_now_add=True)  

    class Meta:
        ordering = ["uploaded_at"]

    def __str__(self):
        return self.name
    
