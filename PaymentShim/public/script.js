window.addEventListener("load",addListener)
var gradeamountnum, amountorgrade, gradetotal, tempcount
function addListener() {
	gradetotal = 0;
	tempcount = 0;
	amountorgrade = true;
    document.getElementById("btnenter").addEventListener("click", checkoperation);
}
function checkoperation() {
	if (amountorgrade == true) {
		gradeamount();
	} else {
		usergrade();
	}
}
function gradeamount() {
	gradeamountnum = parseFloat(document.getElementById("txtinputvalue").value);
	if (gradeamountnum <= 0 || gradeamountnum % 1 != 0) {
		alert("Invalid grade amount");
		document.getElementById("txtinputvalue").value = "";
		document.getElementById("txtinputvalue").focus();
	} else {
		document.getElementById("txtinputvalue").value = "";
		document.getElementById("txtinputvalue").focus();
		document.getElementById("lblmsg").textContent = "Enter a grade: ";
		amountorgrade = false;
	}
}
function usergrade() {
	let gradenum = parseFloat(document.getElementById("txtinputvalue").value);
	if (gradenum <= 100 && gradenum >= 0) {
		for (let i = 0; i < gradeamountnum; i++) {
			gradetotal = gradetotal + gradenum
			gradenum = 0
		}
		tempcount = tempcount + 1;
		document.getElementById("txtinputvalue").value = "";
		document.getElementById("txtinputvalue").focus();
		if (tempcount == gradeamountnum) {
			let gpascale = (gradetotal / tempcount) / 25;
			document.getElementById("lbloutputmsg").textContent = document.getElementById("lbloutputmsg").textContent + gpascale
		}
	} else {
		alert("Invalid grade");
		document.getElementById("txtinputvalue").value = "";
		document.getElementById("txtinputvalue").focus();
	}
}