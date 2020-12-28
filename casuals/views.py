from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.
from .models import *
from .forms import StaffForm, JobForm, CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.

@unauthenticated_user
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get('username')

				group = Group.objects.get(name='educator')
				user.groups.add(group)
				#Added username after video because of error returning customer name if not added
				Educator.objects.create(
					user=user,
					nick_name=user.username,
					)

				messages.success(request, 'Account was created for ' + username)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'casuals/register.html', context)

@unauthenticated_user
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
@admin_only
def home(request):
	return render(request, 'casuals/dashboard.html')

@login_required(login_url='login')
@admin_only
def manager(request):

	availability = Availability.objects.all()
	booking = Booking.objects.all()
	job = Job.objects.all()

	context = {'availability':availability, 'booking':booking, 'job':job}
	return render(request, 'casuals/manager.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['educator'])
def educator(request):
	educator = Educator.objects.all()

	context = {'educator':educator}
	return render(request, 'casuals/educator.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['educator'])
def account(request):
	return render(request, 'casuals/account.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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
@allowed_users(allowed_roles=['admin'])
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
@allowed_users(allowed_roles=['admin'])
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
@allowed_users(allowed_roles=['admin'])
def deleteJob(request, pk):
	job = Job.objects.get(id=pk)
	if request.method == "POST":
		job.delete()
		return redirect('/manager')

	context = {'item':job}
	return render(request, 'casuals/delete.html', context)