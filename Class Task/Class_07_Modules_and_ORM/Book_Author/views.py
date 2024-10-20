from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from Book_Author.models import Book

# Create your views here.

# this is function based view
def my_view(request):
    return HttpResponse('Welcome to django!')


class MyView(View):
    def get(self,request):
        return HttpResponse('Welcome to django from Class!')
    
    
class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"
    
    

    