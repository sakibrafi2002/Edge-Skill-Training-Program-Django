from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView,FormView
from django.urls import reverse_lazy
from books.models import Book
from books.forms import ContactForm

# Create your views here.

# this is function based view
def my_view(request):
    return HttpResponse('Welcome to django!')

# this is class based view
class MyView(View):
    def get(self,request):
        return HttpResponse('Welcome to django from Class!')
    
    
class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"
    
class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')
    
    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)

    