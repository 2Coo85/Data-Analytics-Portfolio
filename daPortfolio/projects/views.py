from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "projects/home.html")

def project(request, project):
    if project == "SQL Project" or project == "Capstone" or project == "Excel Project":
        return HttpResponse("Coming Soon")
    else:
        return HttpResponse("The page you are looking for doesn't exist")

