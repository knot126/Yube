function showLogin() {
	let popup = document.getElementById("login-popup");
	
	popup.style.display = "inherit";
}

function hideLogin() {
	let popup = document.getElementById("login-popup");
	
	popup.style.display = "none";
}

function requestLogin() {
	
}

function startLogin() {
	let request = new XMLHttpRequest();
	let username = document.getElementById("username").value;
	let password = document.getElementById("password").value;
	
	request.addEventListener("load", requestLogin);
	request.open("POST", "/login");
	request.send("");
}
