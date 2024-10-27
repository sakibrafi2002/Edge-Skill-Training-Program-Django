from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField(default="2000-02-02")
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(null = True, blank = True)
    publication_date = models.DateField(null = True, blank = True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.FloatField(default=0.00)
    
    def __str__(self):
        return  self.title
    

class Publisher(models.Model):
    name = models.CharField(max_length=300)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def __str__(self):
        return  self.name