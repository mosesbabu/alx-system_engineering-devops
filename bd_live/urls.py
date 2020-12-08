from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('child/', views.child),
    path('staff/', views.staff),
]