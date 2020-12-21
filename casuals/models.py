from django.db import models

# Create your models here.

class Staff(models.Model):
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

	fname = models.CharField(max_length=200, null=True)
	lname = models.CharField(max_length=200, null=True)
	nname = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	qualification = models.CharField(max_length=200, null=True, choices=QUALIFICATION)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.fname

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