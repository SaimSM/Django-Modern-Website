from django.shortcuts import render, HttpResponse
from .models import TodoItem
# from django.shortcuts import render

def todo(request):
    items = TodoItem.objects.all()   
    return render(request, 'todo.html', {"todo_items": items})

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def base(request):
    return render(request, "base.html")