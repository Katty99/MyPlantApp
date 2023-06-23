from django.urls import path, include

from MyPlantApp.plant_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('create/', views.create_plant, name='create_plant'),
    path('details/<int:plant_id>/', views.plant_details, name='plant_details'),
    path('edit/<int:plant_id>/', views.edit_plant, name='edit_plant'),
    path('delete/<int:plant_id>/', views.delete_plant, name='delete_plant'),
]