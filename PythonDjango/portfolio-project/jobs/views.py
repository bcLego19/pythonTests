from django.shortcuts import render

# Create your views here.
def conner(request):
    return render(request, 'jobs/home.html')