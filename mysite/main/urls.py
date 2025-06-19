from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('contact/', views.contact, name='contact'),
    path('old-contact/', views.old_contact_redirect, name='old_contact'),
    path('not-found/', views.custom_not_found, name='not_found'),
]
