from django.contrib import admin
from django.urls import path

from foods.views import index
from . import views

urlpatterns = [
    path('index/', views.index),
    path('', views.index),
    path('menu/<str:food>/', views.food_detail)
]
