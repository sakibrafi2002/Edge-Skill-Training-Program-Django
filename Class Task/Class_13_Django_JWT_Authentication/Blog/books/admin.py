from django.contrib import admin

# Register your models here.

from .models import Author, Book, Publisher

# Register Author model
admin.site.register(Author)

# Register Book model
admin.site.register(Book)

# Register Publisher model
admin.site.register(Publisher)