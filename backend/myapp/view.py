from django.shortcuts import render, ridirect
from django.http import HttpResponse

def home(request):
    return render(request,"profile.html")