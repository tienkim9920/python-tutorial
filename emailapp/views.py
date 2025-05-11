from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  emails = [
    {
      'title': 'Thong bao lich phong van',
      'description': 'Phong van luc 14h00',
      'time': '04/05/2025',
      'status': False,
    },
    {
      'title': 'Ket qua phong van',
      'description': 'Chuc mung ban',
      'time': '04/05/2025',
      'status': True,
    },
    {
      'title': 'Thong bao lich di lam viec',
      'description': 'Thu 2 den thu 6',
      'time': '04/05/2025',
      'status': True,
    },
  ]
  return render(request, 'home.html', { 'emails': emails })