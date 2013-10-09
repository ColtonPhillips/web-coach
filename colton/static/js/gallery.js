$(function() {

	Galleria.loadTheme("/static/galleria/themes/classic/galleria.classic.min.js");

	Galleria.configure({
		lightbox: true,
		showInfo: false
	});

	Galleria.run("#gallery");
});
