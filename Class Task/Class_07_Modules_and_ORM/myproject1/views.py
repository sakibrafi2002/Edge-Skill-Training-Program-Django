# from django.http import HttpResponse
from django.shortcuts import render



# def hello_django(request):
#     return HttpResponse("Hello Django")

def hello_django(request):
    return render(request,'hello.html')

