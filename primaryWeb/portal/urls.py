from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
	path('login', loginpage),
	path('all', allrequestpage),
	path('new', requestpage),
	path('req', viewrequestpage),
	path('update', updatepage)
]