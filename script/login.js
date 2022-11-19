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
		message.innerHTML = response["message"];
		window.localStorage.setItem("login_token", response["token"]);
		window.localStorage.setItem("login_username", response["username"]);
		updateLoginStatus();
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
	request.open("POST", "/login");
	request.send("{\"type\": \"login\", \"username\": \"" + username + "\", \"password\": \"" + password + "\", \"permissions\": [\"base\", \"interact\", \"subscribe\", \"comment\", \"upload\", \"edit\", \"stats\"]}");
}

function updateLoginStatus() {
	let username = window.localStorage.getItem("login_username");
	let menu = document.getElementById("user-link");
	
	console.log(username, menu);
	
	if (username && menu) {
		menu.innerHTML = "<a href=\"/user/@" + username + "\">" + username + "</a>";
	}
}
