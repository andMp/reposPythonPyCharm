from django.urls import path
from . import views

urlpatterns = [
    path('', views.carad_list, name='carad_list'),
    path('add/', views.carad_create, name='carad_create'),
]
