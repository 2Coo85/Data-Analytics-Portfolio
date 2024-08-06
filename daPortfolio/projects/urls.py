from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('projects/<project>', views.project, name="projectpage"),
    
]
