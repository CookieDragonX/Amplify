from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return render(response, "home/home.html",{})
