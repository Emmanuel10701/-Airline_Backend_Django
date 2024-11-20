from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def add (request):
    return HttpResponse("hello world!")
