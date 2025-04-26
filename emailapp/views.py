from django.http import HttpResponse
from django.shortcuts import render
from .email import get_Email_list

def home(request):
  emails = get_Email_list()
  return render(request, 'home.html', { 'emails': emails })