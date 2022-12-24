function startEditTitle() {
	let feild = document.getElementById("video-title-heading");
	let container = document.getElementById("edit-title-button-container");
	
	feild.contentEditable = true;
	container.innerHTML = '<button id="edit-title-button" class="button-tonal login-only" style="margin-top: 0.5em;" onclick="endEditTitle()">Save title</button>';
}

function afterUpdateTitle() {
	let status = this.status;
	let response = JSON.parse(this.responseText);
	
	if (status == 200) {
		console.log("Title updated okay!");
	}
	else {
		console.log("The title was not updated, error: " + this.responseText);
	}
}

function updateTitle() {
	let request = new XMLHttpRequest();
	let username = window.localStorage.getItem("login_username");
	let token = window.localStorage.getItem("login_token");
	let title = document.getElementById("video-title-heading").innerHTML;
	
	request.addEventListener('loadend', afterUpdateTitle);
	request.open("POST", "/update-video-metadata");
	request.send('"token": "' + token + ', "feild": "title", "data": "' + title + '"}'); // TODO Escape strings
}

function endEditTitle() {
	let feild = document.getElementById("video-title-heading");
	let container = document.getElementById("edit-title-button-container");
	
	feild.contentEditable = false;
	container.innerHTML = '<button id="edit-title-button" class="button-tonal login-only" style="margin-top: 0.5em;" onclick="startEditTitle()">Edit title</button>';
	
	updateTitle();
}

function updateVideoOwner() {
	
}
