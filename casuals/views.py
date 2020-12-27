from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from .forms import StaffForm, JobForm, CreateUserForm

# Create your views here.

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'casuals/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'casuals/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
	return render(request, 'casuals/dashboard.html')

@login_required(login_url='login')
def manager(request):

	availability = Availability.objects.all()
	booking = Booking.objects.all()
	job = Job.objects.all()

	context = {'availability':availability, 'booking':booking, 'job':job}
	return render(request, 'casuals/manager.html', context)

@login_required(login_url='login')
def staff(request):
	staff = Staff.objects.all()

	context = {'staff':staff}
	return render(request, 'casuals/staff.html',context)

@login_required(login_url='login')
def account(request):
	return render(request, 'casuals/account.html')

@login_required(login_url='login')
def createStaff(request):
	form = StaffForm()
	if request.method == 'POST':
		form = StaffForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'casuals/staff_form.html', context)

@login_required(login_url='login')
def createJob(request):
	form = JobForm()
	if request.method == 'POST':
		form = JobForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/manager')

	context = {'form':form}

	return render(request, 'casuals/job_form.html', context)

@login_required(login_url='login')
def updateJob(request, pk):
	job = Job.objects.get(id=pk)
	form = JobForm(instance=job)

	if request.method == 'POST':
		form = JobForm(request.POST, instance=job)
		if form.is_valid():
			form.save()
			return redirect('/manager')

	context = {'form':form}
	return render(request, 'casuals/job_form.html', context)

@login_required(login_url='login')
def deleteJob(request, pk):
	job = Job.objects.get(id=pk)
	if request.method == "POST":
		job.delete()
		return redirect('/manager')

	context = {'item':job}
	return render(request, 'casuals/delete.html', context)