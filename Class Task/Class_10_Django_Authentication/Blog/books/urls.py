from django.urls import path
from django.shortcuts import render
from books.views import my_view, BookListView, MyView, ContactFormView,CreateBookView
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path("initial/", my_view,),
    path("initial_class/", MyView.as_view()),
    path("list/", BookListView.as_view(), name='book_list'),
    path('contact/add', ContactFormView.as_view()),
    path('contact_success/', lambda request: render(request, 'success/contact_success.html'), name='contact_success'),
    path('book/add/', CreateBookView.as_view()),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]