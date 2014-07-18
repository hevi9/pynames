function activateSection(id) {
	// document.getElementsBy
	console.log("HERE" + id);
	var section = document.getElementById(id);
	var sections = document.getElementsByTagName("section");
	var i;
	for (i = 0; i < sections.length; i++) {
		sections[i].removeAttribute("active");
	}
	section.setAttribute("active","");	
}