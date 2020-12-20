from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request, 'casuals/dashboard.html')

def manager(request):
	return render(request, 'casuals/manager.html')

def staff(request):
	return render(request, 'casuals/staff.html')

def availability(request):
	return render(request, 'casuals/availability.html')

def bookings(request):
	return render(request, 'casuals/bookings.html')