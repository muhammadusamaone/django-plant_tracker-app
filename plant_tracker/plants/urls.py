from django.urls import path
from . import   views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.plant_list, name='plant_list'),
    path('add/', views.add_plant, name='add_plant'),
    path('edit/<int:pk>/', views.edit_plant, name='edit_plant'),
    path('delete/<int:pk>/', views.delete_plant, name='delete_plant'),
]
