$(function() {

	$('.project').each(function() {
		var	$this	= $(this),
			$head	= $('.head', $this),
			$body	= $('.body', $this);

		$head.click(function() {
			$body.slideToggle({
				duration: 400
			});
		});
	});
});
