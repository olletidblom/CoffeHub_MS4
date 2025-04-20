from . import views as comment_views
from .models import Product

from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='product-list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('comments/<int:pk>/edit/', comment_views.edit_comment, name='edit_comment'),
    path('comments/<int:pk>/delete/', comment_views.delete_comment, name='delete_comment'),
]