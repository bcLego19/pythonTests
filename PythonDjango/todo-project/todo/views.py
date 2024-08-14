from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todo_list = Todo.objects.all()
    # Use an empty form instance for displaying the form
    form = TodoForm()
    if request.method == 'POST':
        # Create a form instance with the submitted data
        form = TodoForm(request.POST)
        if form.is_valid():
            # Access completed checkboxes using form.cleaned_data['completed']
            completed_ids = request.POST.getlist('completed')  # Get a list of selected checkbox values
            for todo_id in completed_ids:
                todo = Todo.objects.get(pk=todo_id)
                todo.completed = not todo.completed  # Toggle completed status
                todo.save()
            return redirect('/')
    return render(request, 'todo/index.html', {'todo_list': todo_list, 'form': form})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        new_todo = Todo(title=title)
        new_todo.save()
        return redirect('/')
    return render(request, 'todo/add.html')