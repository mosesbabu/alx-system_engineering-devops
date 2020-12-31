from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Educator, Job, Availability, Booking


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class EducatorForm(ModelForm):
	class Meta:
		model = Educator
		fields = '__all__'
		exclude = ['user']


class JobForm(ModelForm):
	class Meta:
		model = Job
		fields = '__all__'
		exclude = ['date_created']

class AvailabilityForm(ModelForm):
	class Meta:
		model = Availability
		fields = '__all__'
		exclude = ['date_created']

class BookingForm(ModelForm):
	class Meta:
		model = Booking
		fields = '__all__'
		exclude = ['date_created', 'availability']		