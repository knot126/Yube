var hover = false;

function playerToggleHover() {
	let controls = document.getElementById("video-controls");
	
	hover = !hover;
	
	// Toggles opacity
	controls.style.opacity = 1.0 - controls.style.opacity;
}

function initPlayer() {
	let video = document.getElementById("video");
	
	video.loop = true;
}

function togglePlay() {
	let video = document.getElementById("video");
	let playButton = document.getElementById("main-play-button");
	
	if (video.paused) {
		video.play();
		playButton.src = "get-resource/pause.svg";
	}
	else {
		video.pause();
		playButton.src = "get-resource/play.svg";
	}
}

function showLogin() {
	let popup = document.getElementById("login-popup");
	
	popup.style.display = "inherit";
}

function hideLogin() {
	let popup = document.getElementById("login-popup");
	
	popup.style.display = "none";
}
