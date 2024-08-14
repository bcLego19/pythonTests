from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todo_list = Todo.objects.all()
    form = TodoForm()
    return render(request, 'todo/index.html', {'form': form})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        new_todo = Todo(title=title)
        new_todo.save()
        return redirect('/')
    return render(request, 'todo/add.html')