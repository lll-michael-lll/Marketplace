from django.urls import path
from . import views

urlpatterns = [
    path('',views.account_page,name='Inventory'),
    path('item_detail_<int:id>/', views.item_detail, name='item_detail'),
    path('<int:id>/edit', views.edit_item, name='edit_item'),
    path('<int:id>/delete', views.delete_item, name='delete_item'),
     path('add_item/',views.add_item, name='add_item'),
    path('add-category/', views.add_category, name='add_category'),
]