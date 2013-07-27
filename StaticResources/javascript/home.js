/* 
 * The javascript below is designed to refresh frames in this page with results modified by the input that users submit through 
 * a html form.  Also, it is used to redirect the bottom page frame to the genetic analysis module that is selected by the user through
 * the top menu on the site
 */

function IframeToSNPMissingness() {
	document.getElementById("GeneticAnalysesFrame").src = "/SNPMissingness/";
}

function IframeToMinorAllele() {
	document.getElementById("GeneticAnalysesFrame").src = "/MinorAllele/";
}

function IframeToHardyWeinberg() {
	document.getElementById("GeneticAnalysesFrame").src = "/HardyWeinberg/";
}

function IframeToChiSquareAssociation() {
	document.getElementById("GeneticAnalysesFrame").src = "/ChiSquareAssociation/";
}

function IframeToPopulationStratification() {
	document.getElementById("GeneticAnalysesFrame").src = "/PopulationStratification/";
}

/* Code to help menu be compatible across browsers */
startList = function() {
	if (document.all && document.getElementById) {
		navRoot = document.getElementById("nav");
		for ( i = 0; i < navRoot.childNodes.length; i++) {
			node = navRoot.childNodes[i];
			if (node.nodeName == "LI") {
				node.onmouseover = function() {
					this.className += " over";
				}
				node.onmouseout = function() {
					this.className = this.className.replace(" over", "");
				}
			}
		}
	}
}

function activateMenuCompatibilityCode() {
	window.onload = startList;
}