function data() {
	return {
		is_headline: '',
		is_headline_full: '',
		content: '',
		headline_title: '',
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
					this.is_headline = response.is_headline;
					this.is_headline_full = response.is_headline_full;
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