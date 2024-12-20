'use strict';

function updateLogo() {
	if ($(window).width() <= 1200) {
		$("#logo").attr('src', logo2Dir).removeClass('logo-1').addClass('logo-2');
	}
	else {
		$("#logo").attr('src', logo1Dir).removeClass('logo-2').addClass('logo-1');
	};
};
function updateMenu() {
	// присвоение .icon
	$('.navbar-nav .nav-item .menu-item').each(function() {
		$(this).find('span.icon-fill').addClass('d-none');
		$(this).find('span.icon').removeClass('d-none');
	});
	// текущему пункту меню - .icon-fill
	$('.navbar-nav .nav-item a').each(function() {
		if (this.href != window.location.href) {
			return;
		};
		let toFill;
		if ($(this).hasClass('sub-menu-item')) {
			toFill = [$(this).find('.menu-item'), $(this).closest('ul.sub-menu').closest('.menu-item')];
		}
		else {
			toFill = [$(this).find('.menu-item')];
		};
		toFill.forEach(function(tag) {
			tag.find('span.icon-fill').removeClass('d-none');
			tag.find('span.icon').addClass('d-none');
		});
		return false;
	});
};

$(window).on('resize', updateLogo);

$(document).ready(function(){
	updateLogo();
	updateMenu();


	const $header = $('header');
	const showNav = "translateY(0%)";
	const closeNav = "translateY(-100%)";
	const headerIndent = 50;
	let prevScrollPos = $(window).scrollTop();
	let isScrollingUp = true;
	let ticking = false;

	// начальная позиция $header
	$header.css('transform', showNav);

	$(window).on('scroll', function() {
		const curScrollPos = $(window).scrollTop();
		// только при изменении
		if (curScrollPos !== prevScrollPos) {
			// оптимизация анимации
			if (!ticking) {
				window.requestAnimationFrame(function() {
					if (curScrollPos < prevScrollPos) {
						// прокрутка вверх
						if (!isScrollingUp) {
							$header.css('transform', showNav);
							isScrollingUp = true;
						}
					} else {
						// прокрутка вниз
						if (isScrollingUp && curScrollPos > headerIndent) {
							$header.css('transform', closeNav);
							isScrollingUp = false;
						}
					}
					prevScrollPos = curScrollPos;
					ticking = false; // событие обработано
				});
				ticking = true;
			};
		};
	});
});