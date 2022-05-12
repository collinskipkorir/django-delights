from django.db import models
import datetime

class Ingredient(models.Model):
    name = models.CharField(max_length=30, default="")
    quantity = models.FloatField(default=0.0)
    unit = models.CharField(max_length=15, default="")
    unit_price = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.name + ": " + self.quantity + " for " + self.unit_price + " per " + self.unit
    
class MenuItem(models.Model):
    title = models.CharField(max_length=100, default="")
    price = models.FloatField(default=1.0)
    
    def __str__(self):
        return self.title + " for " + self.price
    
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(to=MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(to=Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)
    
class Purchase(models.Model):
    menu_item = models.ForeignKey(to=MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.date.today)