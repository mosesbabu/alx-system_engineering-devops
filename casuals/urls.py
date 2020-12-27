from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('staff/', views.staff, name='staff'),
    path('create_staff/', views.createStaff, name='create_staff'),
    path('manager/', views.manager, name='manager'),
    path('account/', views.account, name='account'),
    

    path('availability/', views.availability, name='availability'),
    path('bookings/', views.bookings, name='bookings'),
]    