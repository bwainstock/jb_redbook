var $predictions = $('div#prediction-container'),
    $predictionsdate = $predictions.children('.panel');

$('#sort-newest').click(function() {
	$predictionsdate.sort(function(a,b){
		var an = a.getAttribute('data-date'),
			bn = b.getAttribute('data-date');
		if(an > bn) {
			return 1;
		}
		if(an < bn) {
			return -1;
		}
		return 0;
	});
	$predictionsdate.detach().appendTo($predictions);
});

$('#sort-thumbs-down').click(function() {
	$predictionsdate.sort(function(a,b){
		var an = a.getAttribute('data-down'),
			bn = b.getAttribute('data-down');
		return bn-an
	});
	$predictionsdate.detach().appendTo($predictions);
});

$('#sort-thumbs-up').click(function() {
	$predictionsdate.sort(function(a,b){
		var an = a.getAttribute('data-up'),
			bn = b.getAttribute('data-up');
		if(an > bn) {
			return -1;
		}
		if(an < bn) {
			return 1;
		}
		return 0;
	});
	$predictionsdate.detach().appendTo($predictions);
});
