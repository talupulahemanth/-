from django.db import models

class MenuItem(models.Model):
    DISH_TYPES = [
        ('Veg', 'Vegetarian'),
        ('Non-Veg', 'Non-Vegetarian'),
    ]
    
    dish_name = models.CharField(max_length=100)
    dish_type = models.CharField(max_length=7, choices=DISH_TYPES)
    allergens = models.TextField(blank=True)
    
    def __str__(self):
        return self.dish_name
