'use strict';

const requestToken = '1234';
const loginURL = '/auth/login';
const logoutURL = '/auth/logout';
const registerURL = '/auth/register';
const viewURL = '/auth/view';
const editURL = '/auth/edit';
// const calcURL = '/calculator/';
const blockRequestError = `
	<div class="container w-50 text-center bg-light text-danger border border-5 border-danger rounded-5 m-auto">
		<div class="text">
			Проблема с получением данных,<br>повторите попытку позже.
		</div>
	</div>
`;
const titleRequestError = 'Ошибка';
const logo1Dir = '../static/images/logo1.jpg';
const logo2Dir = '../static/images/logo2.jpg';
// const profileRegisterTitle = 'Регистрация';
// const profileLoginTitle = 'Вход';
// const profileViewTitle = 'Профиль';
// const profileEditTitle = 'Редактирование';