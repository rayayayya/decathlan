from django.db import models

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  
    price = models.IntegerField()  
    description = models.TextField() 
    thumbnail = models.URLField()  
    category = models.CharField(max_length=50) 
    is_featured = models.BooleanField(default=False)  

    # tambahan opsional
    stock = models.PositiveIntegerField(default=0) 
    rating = models.FloatField(default=0.0)  
    brand = models.CharField(max_length=50, blank=True, null=True)  

    def __str__(self):
        return f"{self.name} - {self.category}"


