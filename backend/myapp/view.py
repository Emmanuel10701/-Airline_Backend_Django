from django.shortcuts import render, redirect  # Fixed typo in "redirect"
from django.http import HttpResponse

def home(request):
    return render(request, "profile.html")  # Ensure "profile.html" exists in the templates directory
