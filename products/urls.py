

from django.shortcuts import render
from .models import Product

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product-list'),
]