from django.contrib import admin
from django.urls import path,include
from .import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_django),
    path('books/', include("Book_Author.urls")),
]
