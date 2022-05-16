from django.db import models
import datetime

class Ingredient(models.Model):
    """
    Represents a single ingredient in the restaurant's inventory
    """
    name = models.CharField(max_length=30, default="")
    quantity = models.FloatField(default=0.0)
    unit = models.CharField(max_length=15, default="")
    unit_price = models.FloatField(default=0.0)
    
    def get_absolute_url(self):
        return "/ingredients"
    

    def __str__(self):
        return f"""
        name={self.name};
        qty={self.quantity};
        unit={self.unit};
        unit_price={self.unit_price}
        """
    
class MenuItem(models.Model):
    """
    Represents an entry off the restaurant's menu
    """
    title = models.CharField(max_length=100, default="")
    price = models.FloatField(default=1.0)
    
    def get_absolute_url(self):
            return "/menu"
    
    def available(self):
        return all(X.enough() for X in self.reciperequirement_set.all())
    
    def __str__(self):
        return self.title + " for " + str(self.price)

    
class RecipeRequirement(models.Model):
    """
    Represents an ingredient required for a recipe for a MenuItem
    """
    menu_item = models.ForeignKey(to=MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(to=Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)

    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; ingredient={self.ingredient.name}; qty={self.quantity}"
    
    def get_absolute_url(self):
        return "/menu"

    def enough(self):
        return self.quantity <= self.ingredient.quantity
    
class Purchase(models.Model):
    """
    Represents a purchase of a MenuItem
    """
    menu_item = models.ForeignKey(to=MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; time={self.timestamp}"

    def get_absolute_url(self):
        return "/purchases"