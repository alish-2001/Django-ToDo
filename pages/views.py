from django.shortcuts import render
from django.views import generic
from todo.models import Task
# Create your views here.

class HomeView(generic.TemplateView):
  
  template_name='home.html'

class ContactMeView(generic.TemplateView):
  
  template_name='pages/contact.html'



