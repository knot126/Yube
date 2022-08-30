import files
from template import Template
from database import DatabaseFolder

def watch(self, path, params, kind):
	"""
	Handles watching videos
	"""
	
	# Get video ID from watch?video=$id or watch/$id
	GET_video_id = params.get("video", None) if params else None
	PATH_video_id = path[1] if (len(path) >= 2) else None
	
	video_id = GET_video_id if GET_video_id else PATH_video_id
	
	if (not video_id):
		return # Should 404
	
	# Load the video info from the database
	db = DatabaseFolder("video")
	
	video = db.read(video_id)
	
	if (not video):
		return # Should 404
	
	# Create the page content
	t = Template("video.template")
	t.addVariable("video.title", video["title"])
	t.addVariable("video.date", video["date"])
	t.addFormattedVariable("video.info", video["info"])
	t.addVariable("channel.name", video["name"])
	t.addVariable("channel.lower", '@' + video["lower"])
	content = t.evaluate()
	length = len(content)
	
	# Send the response
	self.send_response(200, "OK")
	self.send_header("Content-Length", str(length))
	self.end_headers()
	
	if (kind == "HEAD"):
		return
	
	self.wfile.write(content)
