from django.urls import path
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from books.views import my_view, BookListView, MyView, ContactFormView,CreateBookView,BookListCreate,BookGetUpdateDelete



urlpatterns = [
    path("initial/", my_view,),
    path("initial_class/", MyView.as_view()),
    path("list/", BookListView.as_view(), name='book_list'),
    path('contact/add', ContactFormView.as_view()),
    path('contact_success/', lambda request: render(request, 'success/contact_success.html'), name='contact_success'),
    path('book/add/', CreateBookView.as_view()),
    path('rest_booklist/', BookListCreate.as_view(), name='rest_book_list'),
    path('rest/book/<int:pk>', BookGetUpdateDelete.as_view(), name='rest_book'),
]