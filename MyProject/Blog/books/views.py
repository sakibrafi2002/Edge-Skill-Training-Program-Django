# from django
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView,FormView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# from books app
from books.models import Book
from books.forms import ContactForm,BookForm

#from rest framework
from rest_framework.response import Response
from rest_framework.views import APIView
from books.serializers import BookSerializer

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
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            context = {'x':1}
            return render(request,'login.html',context)  # Redirect to login if not authenticated
        return super().dispatch(request, *args, **kwargs)

    
class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')
    
    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)

    

# CreateBookView will handle creating a new Book instance using a form
class CreateBookView(CreateView):
    model = Book                      # Specify the model to use
    form_class = BookForm             # Use the custom form we created
    template_name = 'create_book.html'  # Template to render the form
    success_url = reverse_lazy('book_list')  # Redirect after successful form submission
    
    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)


#Rest framework API's
class BookListCreate(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    
