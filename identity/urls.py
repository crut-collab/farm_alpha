from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('register', views.register, name='register'),
	path('login', views.login, name='login'),
	path('view', views.view, name='view'),
	path('edit', views.edit, name='edit'),
	path('logout', views.logout, name='logout'),
]
