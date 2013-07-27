function SubmitForm() {
	$(document).ready(function() {
		$("#FilterExperimentResults").attr('action', 'table');
		$("#FilterExperimentResults").attr('target', 'ExperimentResultsTable');
		$("#FilterExperimentResults").submit();
	});

	document.getElementById("PlotRefreshingMessage").style.visibility = "visible";
	$(document).ready(function() {
		$("#FilterExperimentResults").attr('action', 'plot');
		$("#FilterExperimentResults").attr('target', 'ExperimentResultsPlot');
		$("#FilterExperimentResults").submit();
	});
}


$(document).ready(function() {
	function test() {
		$("#FilterExperimentResults").submit();
	}

});

function CheckDatabaseFilterErrors() {
	if (document.getElementById('FilterThreshold').value >= 1) {
		document.getElementById('FilterThreshold').value = .99;
		document.getElementById("DatabaseFilterInputError").style.visibility = "visible";
		setTimeout(function() {
			document.getElementById("DatabaseFilterInputError").style.visibility = "hidden";
		}, 20000);
	} else if (document.getElementById('FilterThreshold').value < 0) {
		document.getElementById('FilterThreshold').value = 0;
		document.getElementById("DatabaseFilterInputError").style.visibility = "visible";
		setTimeout(function() {
			document.getElementById("DatabaseFilterInputError").style.visibility = "hidden";
		}, 20000);
	}
}