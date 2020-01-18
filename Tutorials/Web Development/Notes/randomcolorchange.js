function init() {
	var h1tags = document.getElementsByTagName("h1"); // Grabs all the h1 tags.
	h1tags[0].onclick = changeColor; // Reference the first one to call changeColor. 
}

function changeColor() {
	this.innerHTML = "Click Again."; // Changes the text of the tag.
	// Generates a random color hex value.
	var randomcolor = '#' + Math.floor(Math.random() * 16777215).toString(16);
	this.style.color = randomcolor;
}

function toggleImg() {
	var img = document.getElementById("danceImg");
	var isImgVisible = img.style.visibility != "visible";
	img.style.visibility = isImgVisible ? "visible" : "hidden";
}

// If you want to execute a function whenever the page is loaded. 
onload = init;