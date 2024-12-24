from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, JsonResponse
from .forms import CreateUserForm, AuthUserForm, ChangeUserForm, ViewUserForm
from django.template.loader import render_to_string
from django.contrib.auth import login, logout


# @login_required
def view(request):
	if request.method != "GET":
		return HttpResponseNotAllowed(['GET'])
	if request.user.is_authenticated:
		form = ViewUserForm(instance=request.user)
	else:
		return redirect('login')

	return JsonResponse({
		'form': render_to_string(
			'dynamic/profile_view.html', 
			{
				'form': form,
			}, 
			request=request
		),
		'title': 'Профиль'
	})

def login(request):
	if request.method == "POST":
		form = AuthUserForm(request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return JsonResponse({
				'redirect': True,
				'url': reverse('home'),
			})
	else:
		form = AuthUserForm()

	return JsonResponse({
		'form': render_to_string(
			'dynamic/profile_login.html', 
			{
				'form': form,
			}, 
			request=request
		),
		'title': 'Ауентификация'
	})

def register(request):
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return JsonResponse({
				'redirect': True,
				'url': reverse('home'),
			})
	else:
		form = CreateUserForm()
	
	return JsonResponse({
		'form': render_to_string(
			'dynamic/profile_register.html', 
			{
				'form': form,
			}, 
			request=request
		),
		'title': 'Регистрация'
	})

@login_required
def edit(request):
	if request.method == "POST":
		form = ChangeUserForm(request.POST)
		if form.is_valid():
			form.save()
			return JsonResponse({
				'redirect': True,
				'url': request.POST['url']
			})
	else:
		form = ChangeUserForm(instance=request.user)
	
	return JsonResponse({
		'form': render_to_string(
			'dynamic/profile_edit.html', 
			{
				'form': form,
			}, 
			request=request
		),
		'title': 'Редактирование'
	})

@login_required
def logout(request):
	if request.method != "POST":
		return HttpResponseNotAllowed(['POST'])

	logout(request)
	return JsonResponse({
		'redirect': True,
		'url': reverse('home')
	})
