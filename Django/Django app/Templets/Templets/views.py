from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')
def about(request):
    # return HttpResponse("Hello, World, You are at First Django App's Home page")
    return HttpResponse("Hello, World, You are at First Django App's About page")
    # return render(request,'index.html')
def contact(request):
    return HttpResponse("Hello, World, You are at First Django App's Contact page")
    # return render(request,'index.html')


