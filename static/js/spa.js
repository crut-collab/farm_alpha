function data() {
	return {
		mainQ: false,
		title: 'Мобильная ферма',
		no_headline: false,
		headline_title: '',
		content: '',
		init() {
			this.loadPage(window.location.pathname);
		},
		loadPage(pageUrl) {
			$.ajax({
				url: `${pageUrl.startsWith('/') ? '' : '/'}${pageUrl}`,
				method: "GET",
				headers: {
					'GetContent': 'true',
				},
				success: (response) => {
					if (typeof response.mainQ === 'boolean') {
						this.mainQ = response.mainQ;
					}
					if (typeof response.no_headline === 'boolean') {
						this.no_headline = response.no_headline;
					}
					this.title = response.title;
					this.content = response.content;
					this.headline_title = response.headline_title;
					window.history.pushState({}, '', pageUrl);
					updateMenu();
				},
				error: (xhr, status, error) => {
					this.content = blockRequestError;
				}
			});
		}
	}
};