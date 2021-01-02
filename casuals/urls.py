from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

	path('', views.home, name='home'),
	path('educator/', views.educator, name='educator'),
	path('educator_list/', views.educatorList, name='educator_list'),
	path('account/', views.account, name="account"),
	path('manager/', views.manager, name='manager'),
	path('staffing/', views.staffing, name='staffing'),

	path('reset_password/',
 		auth_views.PasswordResetView.as_view(template_name="casuals/password_reset/password_reset.html"),
		name="reset_password"),

	path('reset_password_sent/', 
		auth_views.PasswordResetDoneView.as_view(template_name="casuals/password_reset/password_reset_sent.html"), 
		name="password_reset_done"),

	path('reset/<uidb64>/<token>/',
		auth_views.PasswordResetConfirmView.as_view(template_name="casuals/password_reset/password_reset_form.html"), 
		name="password_reset_confirm"),

	path('reset_password_complete/', 
		auth_views.PasswordResetCompleteView.as_view(template_name="casuals/password_reset/password_reset_done.html"), 
		name="password_reset_complete"),

	path('update_educator/<str:pk>/', views.updateEducator, name='update_educator'),
	path('delete_educator/<str:pk>/', views.deleteEducator, name='delete_educator'),	
	path('account/', views.account, name='account'),


	path('create_job/', views.createJob, name='create_job'),
	path('update_job/<str:pk>/', views.updateJob, name='update_job'),
	path('delete_job/<str:pk>/', views.deleteJob, name='delete_job'),

	path('create_availability/', views.createAvailability, name='create_availability'),
	path('update_availability/<str:pk>/', views.updateAvailability, name='update_availability'),
	path('delete_availability/<str:pk>/', views.deleteAvailability, name='delete_availability'),

	path('make_booking/<str:pk>', views.makeBooking, name='make_booking'),
	path('create_booking/', views.createBooking, name='create_booking'),
	path('update_booking/<str:pk>/', views.updateBooking, name='update_booking'),
	path('delete_booking/<str:pk>/', views.deleteBooking, name='delete_booking'),
]