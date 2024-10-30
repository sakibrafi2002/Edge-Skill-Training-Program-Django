from django.contrib import admin
from django.urls import path,include
from user.views import CustomLoginView


urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('books/', include("books.urls")),
    path('user/', include("user.urls")),
]
