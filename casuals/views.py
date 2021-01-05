from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.forms import Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from datetime import date, datetime, timedelta
# Create your views here.
from .models import *
from .forms import *
from .filters import AvailabilityFilter
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
	startdate = date.today()
	enddate = startdate + timedelta(days=14)
	availability_start_today = Availability.objects.filter(date__range=[startdate, enddate]).order_by('date')
	
	booking_start_today = Booking.objects.filter(date__range=[startdate, enddate]).order_by('date')
	job_start_today = Job.objects.filter(date__range=[startdate, enddate]).order_by('date')
	
	availability = Availability.objects.all()
	myFilter = AvailabilityFilter(request.GET, queryset=availability)
	availability = myFilter.qs

	context = {'availability':availability_start_today, 'booking':booking_start_today, 'job':job_start_today, 'myFilter':myFilter}
	return render(request, 'casuals/manager.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['educator'])
def educator(request):
	educator = Educator.objects.all()
	availability = request.user.educator.availability_set.all()
	booking = request.user.educator.booking_set.all()
	job = Job.objects.all()

	context = {'educator':educator, 'availability':availability, 'booking':booking, 'job':job}

	return render(request, 'casuals/educator.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def staffing(request):
	educator = Educator.objects.all()

	context = {'educator':educator}

	return render(request, 'casuals/staffing.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['educator', 'admin'])
def account(request):
	educator = request.user.educator

	form = EducatorForm(instance=educator)

	if request.method == 'POST':
		form = EducatorForm(request.POST, request.FILES,instance=educator)
		if form.is_valid():
			form.save()
			return redirect('/account')

	context = {'form':form}
	return render(request, 'casuals/account.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def educatorList(request):
	educator = Educator.objects.all()

	context = {'educator':educator}
	return render(request, 'casuals/educator_list.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateEducator(request, pk):
	educator = Educator.objects.get(id=pk)
	form = EducatorForm(instance=educator)

	if request.method == 'POST':
		form = EducatorForm(request.POST, instance=educator)
		if form.is_valid():
			form.save()
			return redirect('/staffing')

	context = {'form':form}
	return render(request, 'casuals/account.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteEducator(request, pk):
	educator = Educator.objects.get(id=pk)
	if request.method == "POST":
		educator.delete()
		return redirect('/staffing')

	context = {'item':educator}
	return render(request, 'casuals/delete_educator.html', context)

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

	return render(request, 'casuals/form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['educator'])
def acceptJob(request, pk):
	job = Job.objects.get(id=pk)
	educator = request.user.educator
	form = BookingForm(initial={'educator':educator, 'status':'Accepted'}, instance=job)

	if request.method == "POST":
		form = BookingForm(request.POST)
		if form.is_valid():
			form.save()
			job.delete()
			return redirect('/educator')

	context = {'item':job, 'form':form}

	return render(request, 'casuals/accept_job.html', context)

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
	return render(request, 'casuals/form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteJob(request, pk):
	job = Job.objects.get(id=pk)
	if request.method == "POST":
		job.delete()
		return redirect('/manager')

	context = {'item':job}
	return render(request, 'casuals/delete_job.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['educator'])
def createAvailability(request):
	educator = request.user.educator
	form = AvailabilityForm(initial={'educator': educator})
	if request.method == 'POST':
		form = AvailabilityForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/educator')

	context = {'form':form}

	return render(request, 'casuals/form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['educator'])
def updateAvailability(request, pk):
	availability = Availability.objects.get(id=pk)
	form = AvailabilityForm(instance=availability)

	if request.method == 'POST':
		form = AvailabilityForm(request.POST, instance=availability)
		if form.is_valid():
			form.save()
			return redirect('/educator')

	context = {'form':form}
	return render(request, 'casuals/form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['educator'])
def deleteAvailability(request, pk):
	availability = Availability.objects.get(id=pk)
	if request.method == "POST":
		availability.delete()
		return redirect('/educator')

	context = {'item':availability}
	return render(request, 'casuals/delete_availability.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def makeBooking(request, pk):
	availability = Availability.objects.get(id=pk)
	form = BookingForm(instance=availability)
	if request.method == 'POST':
		form = BookingForm(request.POST)
		if form.is_valid():
			form.save()
			availability.delete()
			return redirect('/manager')

	context = {'form':form}

	return render(request, 'casuals/form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['educator'])
def acceptBooking(request, pk):
	booking = Booking.objects.get(id=pk)
	if request.method == "POST":
		booking.status = 'Accepted'
		booking.save()
		return redirect('/educator')

	context = {'item':booking}

	return render(request, 'casuals/accept_job.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['educator'])
def rejectBooking(request, pk):
	booking = Booking.objects.get(id=pk)
	if request.method == "POST":
		booking.status = 'Not Accepted'
		booking.save()
		return redirect('/educator')

	context = {'item':booking}

	return render(request, 'casuals/reject_job.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createBooking(request):
	form = BookingForm()
	if request.method == 'POST':
		form = BookingForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/manager')

	context = {'form':form}

	return render(request, 'casuals/form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateBooking(request, pk):
	booking = Booking.objects.get(id=pk)
	form = BookingForm(instance=booking)

	if request.method == 'POST':
		form = BookingForm(request.POST, instance=booking)
		if form.is_valid():
			form.save()
			return redirect('/manager')

	context = {'form':form}
	return render(request, 'casuals/form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteBooking(request, pk):
	booking = Booking.objects.get(id=pk)
	if request.method == "POST":
		booking.delete()
		return redirect('/manager')

	context = {'item':booking}
	return render(request, 'casuals/delete_booking.html', context)