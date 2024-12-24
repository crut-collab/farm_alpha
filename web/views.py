from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, JsonResponse, HttpResponseBadRequest
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import login, logout
from django.template.loader import render_to_string

BASE_CONFIG = {'testQ': settings.DEBUG}

def home(request):
	config = BASE_CONFIG | {}
	if 'GetContent' in request.headers:
		return JsonResponse({
			'title': "Домашнаяя",
			'content': render_to_string('dynamic/main_home.html', config), 
			'mainQ': True,
			'no_headline': False,
		})
	return render(request, 'base/base.html', config)

def about(request):
	config = BASE_CONFIG | {}
	if 'GetContent' in request.headers:
		return JsonResponse({
			'title': "О нас",
			'content': render_to_string('dynamic/main_about.html', config), 
			'mainQ': False,
			'no_headline': False,
			'headline_title': "О нас",
		})
	return render(request, 'base/base.html', config)

def contacts(request):
	config = BASE_CONFIG | {}
	if 'GetContent' in request.headers:
		return JsonResponse({
			'title': "Контакты",
			'content': render_to_string('dynamic/main_contacts.html', config), 
			'mainQ': False,
			'no_headline': False,
			'headline_title': "Контакты",
		})
	return render(request, 'base/base.html', config)

# def buy(request):
# 	return HttpResponse("Trying to buy.")

# def profile(request, action: str):
# 	"""

# 	"""
	
# 	token = request.headers.get('X-Server-Token')
# 	if token != settings.SECRET_SERVER_TOKEN:
# 		return HttpResponseForbidden("В доступе отказано!")


# def get_profile(request, action: str):
# 	"""
	
# 	"""
# 	# Проверка токена
# 	token = request.headers.get('X-Server-Token')
# 	if token != settings.SECRET_SERVER_TOKEN:
# 		return HttpResponseForbidden("В доступе отказано!")

# 	form = None
# 	if request.user.is_authenticated:
# 		if request.method == "POST":
# 			match action:
# 				case 'edit':
# 					form, action, title = ChangeUserForm(request.POST, instance=request.user), 'edit', 'Редактирование'
# 					if form.is_valid():
# 						form.save()
# 						return JsonResponse({
# 							'redirect': True,
# 							'url': request.POST['url']
# 						})
# 				case 'logout':
# 					logout(request)
# 					return JsonResponse({
# 						'redirect': True,
# 						'url': reverse('home')
# 					})
# 				case _:
# 					return HttpResponseNotFound("Неизвестный запрос! Проверьте параметры или метод запроса.")
# 		else:
# 			match action:
# 				case 'view':
# 					form, action, title = ViewUserForm(instance=request.user), 'view', 'Профиль'
# 				case 'edit':
# 					form, action, title = ChangeUserForm(instance=request.user), 'edit', 'Редактирование'
# 				case _:
# 					return HttpResponseNotFound("Неизвестный запрос! Проверьте параметры или метод запроса.")
# 	else:
# 		if request.method == "POST":
# 			match action:
# 				case 'register':
# 					form, action, title = CreateUserForm(request.POST), 'register', 'Регистрация'
# 					if form.is_valid():
# 						user = form.save()
# 						login(request, user)
# 						return JsonResponse({
# 							'redirect': True,
# 							'url': reverse('home'),
# 						})
# 				case 'login':
# 					form, action, title = AuthUserForm(request.POST), 'login', 'Ауентификация'
# 					if form.is_valid():
# 						user = form.get_user()
# 						login(request, user)
# 						return JsonResponse({
# 							'redirect': True,
# 							'url': reverse('home'),
# 						})
# 				case _:
# 					return HttpResponseNotFound("Неизвестный запрос! Проверьте параметры или метод запроса.")
# 		else:
# 			match action:
# 				case 'register':
# 					form, action, title = CreateUserForm(), 'register', 'Регистрация'
# 				case 'login':
# 					form, action, title = AuthUserForm(), 'login', 'Ауентификация'
# 				case _:
# 					return HttpResponseNotFound("Неизвестный запрос! Проверьте параметры или метод запроса.")

# 	# if form is None:
# 	# 	pass

# 	return JsonResponse({
# 		'form': render_to_string(
# 			'components/profile_form.html', 
# 			{
# 				'form': form, 
# 				'action': action
# 			}, 
# 			request=request
# 		),
# 		'title': title
# 	})

def operations(request):
	if request.method == "POST":
		pass
	else:
		pass
	return render(request, 'operations.html', {'testQ': settings.DEBUG})