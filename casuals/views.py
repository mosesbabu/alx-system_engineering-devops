from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import StaffForm

# Create your views here.

def home(request):
	return render(request, 'casuals/dashboard.html')

def manager(request):
	return render(request, 'casuals/manager.html')

def staff(request):
	staff = Staff.objects.all

	context = {'staff':staff}
	return render(request, 'casuals/staff.html',context)

def account(request):
	return render(request, 'casuals/account.html')

def createStaff(request):
	form = StaffForm()
	if request.method == 'POST':
		form = StaffForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'casuals/staff_form.html', context)

def availability(request):
	return render(request, 'casuals/availability.html')

def bookings(request):
	return render(request, 'casuals/bookings.html')