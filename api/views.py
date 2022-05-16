from inventory.models import Ingredient, MenuItem, Purchase, RecipeRequirement
from rest_framework import generics
from .serializers import IngredientSerializer, MenuItemSerializer, PurchaseSerializer, RecipeRequirementSerializer

class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    
class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    
class RecipeRequirementList(generics.ListCreateAPIView):
    queryset = RecipeRequirement.objects.all()
    serializer_class = RecipeRequirementSerializer
    
class RecipeRequirementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecipeRequirement.objects.all()
    serializer_class = RecipeRequirementSerializer
    
class PurchaseList(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    
class PurchaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    
class MenuItemList(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
