from django.contrib.auth.models import User, Group
from rest_framework import serializers
from inventory.models import Ingredient, MenuItem, Purchase, RecipeRequirement

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'  
        
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'  
        
class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'  
        
class RecipeRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeRequirement
        fields = '__all__'  
        
