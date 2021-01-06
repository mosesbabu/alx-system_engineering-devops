from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Educator, Job, Availability, Booking
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput


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
		widgets = {
			'date': DatePickerInput(format='%Y-%m-%d'),
			'shift_start_time':TimePickerInput().start_of('shift'),
			'shift_end_time':TimePickerInput().end_of('shift'),
		}		

class AvailabilityForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(AvailabilityForm, self).__init__(*args, **kwargs)
		self.fields['educator'].widget.attrs['readonly'] = True
		widget=forms.Select(attrs={'disabled':'disabled'})

	class Meta:
		model = Availability
		fields = '__all__'
		exclude = ['date_created']
		widgets = {
            'date': DatePickerInput(format='%Y-%m-%d'),
			'start_time':TimePickerInput().start_of('available time'),
            'end_time':TimePickerInput().end_of('available time'),
        }

class BookingForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(BookingForm, self).__init__(*args, **kwargs)
		self.fields['educator'].widget.attrs['readonly'] = True
		widget=forms.Select(attrs={'disabled':'disabled'})

	class Meta:
		model = Booking
		fields = '__all__'
		exclude = ['date_created', 'availability']
		widgets = {
			'date': DatePickerInput(format='%Y-%m-%d'),
			'shift_start_time':TimePickerInput().start_of('shift'),
			'shift_end_time':TimePickerInput().end_of('shift'),
		}				