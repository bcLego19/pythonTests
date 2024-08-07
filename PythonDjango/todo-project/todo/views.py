from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todo_list = Todo.objects.all()
    return render(request, 'todo/index.html', {'todo_list': todo_list})
