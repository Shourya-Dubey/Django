from django.http import HttpResponse
from django.shortcuts import render




def home(request):
    # return HttpResponse("Hello, world. You are at chai aur Django Home Page")
    return render(request, 'website/index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return HttpResponse("Hello, world. You are at chai aur Django Contact Page")

def tag(request):
    return HttpResponse("This Page is for Tag")