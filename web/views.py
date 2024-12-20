from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import login, logout
# from .forms import CreateUserForm, AuthUserForm, ChangeUserForm, ViewUserForm
from django.template.loader import render_to_string


def home(request):
	config = {'testQ': settings.DEBUG}
	if request.headers.get('GetContent', None) and request.headers.get('GetContent') == 'true':
		return JsonResponse({
			'content': render_to_string('components/main_home.html', config), 
			'is_headline': False,
			'is_headline_full': True,
			'headline_title': config.get('headline_title')
		})
	return render(request, 'home.html', config)

def about(request):
	config = {'testQ': settings.DEBUG, 'headline_title': 'О нас'}
	if request.headers.get('GetContent', None) and request.headers.get('GetContent') == 'true':
		return JsonResponse({
			'content': render_to_string('components/main_about.html', config), 
			'is_headline': True,
			'is_headline_full': False,
			'headline_title': config.get('headline_title')
		})
	return render(request, 'about.html', config)

def contacts(request):
	config = {'testQ': settings.DEBUG, 'headline_title': 'Контакты'}
	if request.headers.get('GetContent', None) and request.headers.get('GetContent') == 'true':
		return JsonResponse({
			'content': render_to_string('components/main_contacts.html', config), 
			'is_headline': True,
			'is_headline_full': False,
			'headline_title': config.get('headline_title')
		})
	return render(request, 'contacts.html', config)

# def buy(request):
# 	return HttpResponse("Trying to buy.")



def get_profile(request, action: str):
	"""
	
	"""
	# проверка токена
	token = request.headers.get('X-Server-Token')
	if token != settings.SECRET_SERVER_TOKEN:
		return HttpResponseForbidden("В доступе отказано!")

	form = None
	if request.user.is_authenticated:
		if request.method == "POST":
			match action:
				case 'edit':
					form, action, title = ChangeUserForm(request.POST, instance=request.user), 'edit', 'Редактирование'
					if form.is_valid():
						form.save()
						return JsonResponse({
							'redirect': True,
							'url': request.POST['url']
						})
				case 'logout':
					logout(request)
					return JsonResponse({
						'redirect': True,
						'url': reverse('home')
					})
				case _:
					return HttpResponseNotFound("Неизвестный запрос! Проверьте параметры или метод запроса.")
		else:
			match action:
				case 'view':
					form, action, title = ViewUserForm(instance=request.user), 'view', 'Профиль'
				case 'edit':
					form, action, title = ChangeUserForm(instance=request.user), 'edit', 'Редактирование'
				case _:
					return HttpResponseNotFound("Неизвестный запрос! Проверьте параметры или метод запроса.")
	else:
		if request.method == "POST":
			match action:
				case 'register':
					form, action, title = CreateUserForm(request.POST), 'register', 'Регистрация'
					if form.is_valid():
						user = form.save()
						login(request, user)
						return JsonResponse({
							'redirect': True,
							'url': reverse('home'),
						})
				case 'login':
					form, action, title = AuthUserForm(request.POST), 'login', 'Ауентификация'
					if form.is_valid():
						user = form.get_user()
						login(request, user)
						return JsonResponse({
							'redirect': True,
							'url': reverse('home'),
						})
				case _:
					return HttpResponseNotFound("Неизвестный запрос! Проверьте параметры или метод запроса.")
		else:
			match action:
				case 'register':
					form, action, title = CreateUserForm(), 'register', 'Регистрация'
				case 'login':
					form, action, title = AuthUserForm(), 'login', 'Ауентификация'
				case _:
					return HttpResponseNotFound("Неизвестный запрос! Проверьте параметры или метод запроса.")

	# if form is None:
	# 	pass

	return JsonResponse({
		'form': render_to_string(
			'components/profile_form.html', 
			{
				'form': form, 
				'action': action
			}, 
			request=request
		),
		'title': title
	})

def operations(request):
	if request.method == "POST":
		pass
	else:
		pass
	return render(request, 'operations.html', {'testQ': settings.DEBUG})
