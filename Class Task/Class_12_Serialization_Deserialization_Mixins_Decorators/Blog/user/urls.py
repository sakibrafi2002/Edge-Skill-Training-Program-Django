from django.urls import path
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from .views import RegisterView,CustomLoginView
from . import views



urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogout, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]