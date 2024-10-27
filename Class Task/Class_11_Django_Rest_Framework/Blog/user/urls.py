from django.urls import path
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from .views import RegisterView,CustomLoginView



urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]