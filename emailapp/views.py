from django.http import JsonResponse
from django.shortcuts import render, redirect
from .email import get_Email_list, get_Email_by_id, delete_Email_by_id
from .models import Email

def home(request):
  query = request.GET.get('q')
  emails = Email.objects.all()

  if query:
    emails = [email for email in emails if query.lower() in email.title.lower()]

  return render(request, 'home.html', { 'emails': emails })

def detail_email(request, id):
  email = Email.objects.get(id=id)
  return render(request, 'detail_email.html', { 'email': email })

def search_email(request):
  query = request.GET.get('q')
  page = request.GET.get('page', 1)

  return JsonResponse({
    'query': query,
    'page': page
  })

def delete_email(request, id):
  if request.method == 'POST':
    email = Email.objects.get(id=id)
    email.delete()
    print(f"Da xoa thanh cong")
  return redirect('home')