from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('post/<int:id>/', views.post_detail),
    path('create/', views.create_post), 
    path('edit/<int:id>/', views.edit_post),
    path('delete/<int:id>/', views.delete_post), 
]