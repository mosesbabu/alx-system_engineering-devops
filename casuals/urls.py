from django.urls import path
from . import views


urlpatterns = [

	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

	path('', views.home, name='home'),
	path('educator/', views.educator, name='educator'),
	path('account/', views.account, name="account"),
	path('manager/', views.manager, name='manager'),
	path('staffing/', views.staffing, name='staffing'),
	path('update_educator/<str:pk>/', views.updateEducator, name='update_educator'),
	path('delete_educator/<str:pk>/', views.deleteEducator, name='delete_educator'),	
	path('account/', views.account, name='account'),


	path('create_job/', views.createJob, name='create_job'),
	path('update_job/<str:pk>/', views.updateJob, name='update_job'),
	path('delete_job/<str:pk>/', views.deleteJob, name='delete_job'),

	path('create_availability/', views.createAvailability, name='create_availability'),
	path('update_availability/<str:pk>/', views.updateAvailability, name='update_availability'),
	path('delete_availability/<str:pk>/', views.deleteAvailability, name='delete_availability'),

	path('create_booking/', views.createBooking, name='create_booking'),
	path('update_booking/<str:pk>/', views.updateBooking, name='update_booking'),
	path('delete_booking/<str:pk>/', views.deleteBooking, name='delete_booking'),
]