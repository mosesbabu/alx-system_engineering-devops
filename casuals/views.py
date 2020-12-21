from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
	return render(request, 'casuals/dashboard.html')

def manager(request):
	return render(request, 'casuals/manager.html')

def staff(request):
	staff = Staff.objects.all()
	return render(request, 'casuals/staff.html', {'staff':staff})

def availability(request):
	return render(request, 'casuals/availability.html')

def bookings(request):
	return render(request, 'casuals/bookings.html')