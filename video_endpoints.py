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
	t.addVariable("video.id", video_id)
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

def toInt2(n):
	"""
	Alternate toInt for parseRange
	"""
	
	if (n): return int(n)
	return None

##
## TODO: Support for multipule ranges
##

def parseRange(string):
	"""
	Parse HTTP/1.1 range string
	"""
	
	part = string.split("=")[1].split("-")
	
	return [toInt2(part[i]) for i in range(len(part))]

def get_video_data(self, path, params, kind):
	"""
	Get the video data, or at least one range of video data
	"""
	
	db = DatabaseFolder("video_storage")
	size = db.get_size(path[1])
	part = self.headers.get("Range", None)
	
	if (part == None):
		self.send_response(200, "OK")
		self.send_header("Accept-Ranges", "bytes")
		self.send_header("Content-Length", str(size))
		self.end_headers()
		
		if (kind == "HEAD"):
			return
		
		content = db.read_bytes(path[1], 0, size)
		self.wfile.write(content)
	else:
		part = parseRange(part)
		
		# Find start and end
		start = part[0]
		end = part[1] if part[1] else (size - 1)
		
		self.send_response(206, "Partial content")
		self.send_header("Accept-Ranges", "bytes")
		self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
		self.send_header("Content-Length", str(end - start + 1))
		self.end_headers()
		
		if (kind == "HEAD"):
			return
		
		content = db.read_bytes(path[1], start, end + 1)
		self.wfile.write(content)
