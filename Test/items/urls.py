from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.items,name='Items'),
    path('product_<int:item_id>/', views.item, name='item'),# URL for individual item
    path('filter1/', views.filter1, name='filter1'),# URL for category
    
]