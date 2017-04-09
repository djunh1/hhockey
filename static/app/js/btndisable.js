$(document).ready(function() {
    $('form').submit(function() {
				$(this).find("button[id='place-order']").prop('disabled',true);
	});

});
