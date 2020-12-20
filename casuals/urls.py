from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('staff/', views.staff, name='staff'),
    path('manager/', views.manager, name='manager'),

    path('availability/', views.availability, name='availability'),
    path('bookings/', views.bookings, name='bookings'),
]