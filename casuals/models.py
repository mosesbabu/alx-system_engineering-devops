from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Educator(models.Model):
	QUALIFICATION = (
			('Working Towards Cert III', 'Working Towards Cert III'),
			('Cert III', 'Cert III'),
			('Working Towards Diploma', 'Working Towards Diploma'),
			('Diploma', 'Diploma'),
			('Working Towards Degree', 'Working Towards Degree'),
			('Degree', 'Degree'),
			('Working Towards Master Degree', 'Working Towards Master Degree'),
			('Master Degree', 'Master Degree'),
			('Others', 'Others'),
			)

	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200, null=True)
	last_name = models.CharField(max_length=200, null=True)
	nick_name = models.CharField(max_length=200, null=True)
	mobile = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	qualification = models.CharField(max_length=200, null=True, choices=QUALIFICATION)
	profile_pic = models.ImageField(default="profile.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return f'{self.first_name} {self.last_name} ({self.nick_name})'
		

class Manager(models.Model):
	CENTRE = (
			('Clifton Hill', 'Clifton Hill'),
			('Forest Hill', 'Forest Hill'),
			('Kew', 'Kew'),
			('Richmond', 'Richmond'),            
			) 

	centre = models.CharField(max_length=200, null=True, choices=CENTRE)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.centre


class Availability(models.Model):
	
	educator = models.ForeignKey(Educator, null=True, on_delete= models.SET_NULL)
	date = models.DateField(null=True)
	start_time = models.TimeField(default='06:30', null=True)
	end_time = models.TimeField(default='18:30', null=True)
	time_created = models.DateTimeField(auto_now_add=True, null=True)


class Job(models.Model):
	QUALIFICATION = (
			('Cert III or above', 'Cert III or above'),
			('Diploma or above', 'Diploma or above'),
			)

	manager = models.ForeignKey(Manager, null=True, on_delete= models.SET_NULL)
	date = models.DateField(null=True)
	shift_start_time = models.TimeField(default='06:30', null=True)
	shift_end_time = models.TimeField(default='18:30', null=True)
	qualification = models.CharField(max_length=200, null=True, choices=QUALIFICATION)
	date_created = models.DateTimeField(auto_now_add=True, null=True)


class Booking(models.Model):
	STATUS = (
		('Pending', 'Pending'),
		('Accepted', 'Accepted'),
		('Not Accepted', 'Not Accepted'),
		)

	educator = models.ForeignKey(Educator, null=True, on_delete= models.SET_NULL)
	date = models.DateField(null=True)
	shift_start_time = models.TimeField(null=True)
	shift_end_time = models.TimeField(null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	time_created = models.DateTimeField(auto_now_add=True, null=True)
