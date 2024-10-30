# Django
from django.contrib.auth import views as auth_views
from django.urls import path
# restframework
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import RegisterView, CustomLoginView, LogoutView
from . import views



urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogout, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/logout/', LogoutView.as_view(), name='token_logout'),
]