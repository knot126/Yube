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

function secondsToString(sec) {
	/**
	 * Convert seconds to a formatted string
	 */
	
	let t = Math.floor(sec);
	
	let minute = Math.floor(t / 60);
	let second = t % 60;
	
	if (second < 10) {
		second = "0" + String(second);
	}
	
	return String(minute) + ":" + String(second);
}

function updateProgress() {
	let bar = document.getElementById("main-controls-progress");
	let video = document.getElementById("video");
	let time = document.getElementById("main-controls-time");
	
	bar.style.width = String((video.currentTime / video.duration) * 100.0) + "%";
	time.innerHTML = secondsToString(video.currentTime) + " / " + secondsToString(video.duration);
}

setInterval(updateProgress, 16);
