from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')
def info(request):
    return render(request, 'aboutMe.html')
def projects(request):
    return render(request, 'projects.html')
def poems(request):
    return render(request, 'poems.html')
def food(request):
    return render(request, 'food.html')
    