from django.urls import path
from Book_Author.views import my_view, BookListView, MyView



urlpatterns = [
    path("initial/", my_view,),
    path("initial_class/", MyView.as_view(), name='CBV_example'),
    path("list/", BookListView.as_view())
   
    
]