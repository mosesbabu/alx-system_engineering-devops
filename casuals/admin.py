from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Educator)
admin.site.register(Manager)
admin.site.register(Availability)
admin.site.register(Job)
admin.site.register(Booking)