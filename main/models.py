import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('football', 'Football'),
        ('basketball', 'Basketball'),
        ('badminton', 'Badminton'),
        ('running', 'Running'),
        ('training', 'Training'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('tennis', 'Tennis'),
        ('golf', 'Golf'),
        ('outdoor', 'Outdoor'),
        ('fitness', 'Fitness'),
        ('yoga', 'Yoga'),
        ('skateboarding', 'Skateboarding'),
        ('surfing', 'Surfing'),
        ('hiking', 'Hiking'),
        ('climbing', 'Climbing'),
        ('water_sports', 'Water Sports'),
        ('winter_sports', 'Winter Sports'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)  
    price = models.CharField(max_length=20, blank = False, null = False)  
    description = models.TextField() 
    thumbnail = models.URLField(blank=True, null=True)  
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    stock = models.PositiveIntegerField(default=0)  
    brand = models.CharField(max_length=50, blank=True, null=True)  
    product_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.category}"
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()

    def get_price_rupiah(self):
        return "Rp {:,}".format(int(self.price)).replace(",", ".")

    