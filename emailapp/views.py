from django.http import JsonResponse
from django.shortcuts import render, redirect
from .email import get_Email_list, get_Email_by_id, delete_Email_by_id

def home(request):
  query = request.GET.get('q')
  emails = get_Email_list()

  if query:
    emails = [email for email in emails if query.lower() in email.title.lower()]

  return render(request, 'home.html', { 'emails': emails })

def detail_email(request, id):
  email = get_Email_by_id(id)
  return render(request, 'detail_email.html', { 'email': email })

def search_email(request):
  query = request.GET.get('q')
  page = request.GET.get('page', 1)

  return JsonResponse({
    'query': query,
    'page': page
  })

def delete_email(request, pk):
  if request.method == 'POST':
    delete_Email_by_id(pk)
  return redirect('home')