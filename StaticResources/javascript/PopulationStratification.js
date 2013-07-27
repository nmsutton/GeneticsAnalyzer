function SubmitForm() {
	document.getElementById("PlotRefreshingMessage").style.visibility = "visible";
	$(document).ready(function() {
		$("#FilterExperimentResults").attr('action', 'plot');
		$("#FilterExperimentResults").attr('target', 'ExperimentResultsPlot');
		$("#FilterExperimentResults").submit();
	});
}

function CheckDatabaseFilterErrors() {
	if (document.getElementById('FilterThreshold').value >= .03) {
		document.getElementById('FilterThreshold').value = .03;
		document.getElementById("DatabaseFilterInputError").style.visibility = "visible";
		setTimeout(function() {
			document.getElementById("DatabaseFilterInputError").style.visibility = "hidden";
		}, 20000);
	} else if (document.getElementById('FilterThreshold').value <= -.03) {
		document.getElementById('FilterThreshold').value = -.03;
		document.getElementById("DatabaseFilterInputError").style.visibility = "visible";
		setTimeout(function() {
			document.getElementById("DatabaseFilterInputError").style.visibility = "hidden";
		}, 20000);
	}
}