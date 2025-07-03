from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.contrib.auth.views import LogoutView
class LogoutGetAllowedView(LogoutView):
    http_method_names = ['get', 'post']

urlpatterns = [
    path('', views.carad_list, name='carad_list'),
    path('profile/add/', views.carad_create, name='carad_create'),

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(next_page='carad_list'), name='logout'),

    path('edit/<int:pk>/', views.carad_edit, name='carad_edit'),

    path('profile/', views.profile, name='profile'),
]
