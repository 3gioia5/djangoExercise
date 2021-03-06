from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request, 'cities/index.html')

def city_detail(request, city):
  path_template = 'cities/'

  if city == 'seoul':
    path_template += 'seoul.html'
  elif city == 'paris':
    path_template += 'paris.html'
  elif city == 'tokyo':
    path_template += 'tokyo.html'
  else:
    path_template += 'index.html'
  return render(request, path_template)