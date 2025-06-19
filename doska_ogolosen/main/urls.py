from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:id>/', views.ads_by_category, name='ads_by_category'),
    path('ad/<int:id>/', views.ad_detail, name='ad_detail'),
    path('ad/<int:id>/respond/', views.respond_to_ad, name='respond_to_ad'),
    path('create/', views.create_ad, name='create_ad'),
]
