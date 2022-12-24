from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('This is my first project')

def amma(request):
    return HttpResponse('<h3>Amma is my favourite</h3>')

def nanna(request):
    return HttpResponse('<marquee>Nanna loves me more</marquee>')
