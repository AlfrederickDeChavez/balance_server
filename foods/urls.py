from django.urls import path
from .views import FoodView

urlpatterns = [
    path('consumed/', FoodView.as_view(), name='foods-list')
]

