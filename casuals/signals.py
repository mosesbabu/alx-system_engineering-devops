from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Educator

def educator_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='educator')
		instance.groups.add(group)
		Educator.objects.create(
			user=instance,
			name=instance.username,
			)
		print('Profile created!')

post_save.connect(educator_profile, sender=User)