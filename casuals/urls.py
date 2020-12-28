from django.urls import path
from . import views


urlpatterns = [

	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

	path('', views.home, name='home'),
	path('educator/', views.educator, name='educator'),
	path('create_staff/', views.createStaff, name='create_staff'),
	path('manager/', views.manager, name='manager'),
	path('account/', views.account, name='account'),


	path('create_job/', views.createJob, name='create_job'),
	path('update_job/<str:pk>/', views.updateJob, name='update_job'),
	path('delete_job/<str:pk>/', views.deleteJob, name='delete_job'),
]