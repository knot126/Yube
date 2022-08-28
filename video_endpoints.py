import files
from template import Template

fake_db_entries = {
	"PROkfP3tpXrQrth_uZ0NQM0u": {
		"title": "Some viedeo :D",
		"date": "2022-06-10T13:10:03+00:00:00",
		"lower": "knot126",
		"name": "Knot",
		"info": "This is the equal to the description of a video!!!\n\nHas a lots of stuff!!!",
	},
}

def watch(self, path, params):
	"""
	Handles watching videos
	"""
	
	video = fake_db_entries[params["video"]]
	
	t = Template("video.template")
	t.addVariable("video.title", video["title"])
	t.addVariable("video.date", video["date"])
	t.addVariable("video.info", video["info"])
	t.addVariable("channel.name", video["name"])
	t.addVariable("channel.lower", '@' + video["lower"])
	content = t.evaluate()
	length = len(content)
	
	# Send the response
	self.send_response(200, "OK")
	self.send_header("Content-Length", str(length))
	self.end_headers()
	self.wfile.write(content)
