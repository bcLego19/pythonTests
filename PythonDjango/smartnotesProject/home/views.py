from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Notes

# Create your views here.
def home(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})

@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})

def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})