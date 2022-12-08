function startEditTitle() {
	let feild = document.getElementById("video-title-heading");
	let button = document.getElementById("edit-title-button");
	
	feild.contentEditable = true;
	button.innerHTML = "Save title";
}

function endEditTitle() {
	let feild = document.getElementById("video-title-heading");
	let button = document.getElementById("edit-title-button");
	
	feild.contentEditable = false;
	button.innerHTML = "Edit title";
}

function updateVideoOwner() {
	
}
