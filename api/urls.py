from django.conf.urls import url
from django.urls import path, include
from api import views

urlpatterns = [
    path('ingredient/', views.IngredientList.as_view()),
    path('ingredient/<int:pk>', views.IngredientDetail().as_view()),
    path('menuitem/', views.MenuItemList.as_view()),
    path('menuitem/<int:pk>', views.MenuItemDetail().as_view()),
    path('purchase/', views.PurchaseList.as_view()),
    path('purchase/<int:pk>', views.PurchaseDetail().as_view()),
    path('recipe/', views.RecipeRequirementList.as_view()),
    path('recipe/<int:pk>', views.RecipeRequirementDetail().as_view()),
]

