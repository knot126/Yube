function showLogin() {
	let popup = document.getElementById("login-popup");
	
	popup.style.display = "inherit";
}

function hideLogin() {
	let popup = document.getElementById("login-popup");
	
	popup.style.display = "none";
}

function requestLogin() {
	let status = this.status;
	let message = document.getElementById("login-message");
	let response = JSON.parse(this.responseText);
	
	if (status == 200) {
		message.innerHTML = "Login successful.";
		hideLogin();
	}
	else if (status == 404 || status == 501) {
		message.innerHTML = "The API that is being used to login is not implemented. Please try again or contact support.";
	}
	else {
		message.innerHTML = "Error: " + response["message"];
	}
}

function startLogin() {
	let request = new XMLHttpRequest();
	let username = document.getElementById("username").value;
	let password = document.getElementById("password").value;
	
	request.addEventListener("loadend", requestLogin);
	request.open("POST", "/login", false);
	request.send("{\"type\": \"login\", \"username\": \"" + username + "\", \"password\": \"" + password + "\", \"permissions\": [\"base\", \"interact\", \"subscribe\", \"comment\", \"upload\", \"edit\", \"stats\"]}");
}
