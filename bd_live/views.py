from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request, 'bd_live/dashboard.html')

def child(request):
	return render(request, 'bd_live/child.html')

def staff(request):
	return render(request, 'bd_live/staff.html')