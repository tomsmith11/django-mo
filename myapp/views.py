from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("This site will be used to showcase my django development, and will likely not work properly or function like a normal website for a while.")