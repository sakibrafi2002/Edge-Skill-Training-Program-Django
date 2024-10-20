from django.urls import path
from books.views import my_view, BookListView, MyView



urlpatterns = [
    path("initial/", my_view,),
    path("initial_class/", MyView.as_view()),
    path("list/", BookListView.as_view()),
   
    
]