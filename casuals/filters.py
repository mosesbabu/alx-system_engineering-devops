import django_filters

from .models import *

class AvailabilityFilter(django_filters.FilterSet):
	class Meta:
		model = Availability
		fields = '__all__'
		exclude = ['start_time', 'end_time', 'time_created']