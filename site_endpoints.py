import files
from template import Template

def not_found(self, path, params):
	"""
	Send a file not found error code and page
	"""
	
	self.send_response(404, "File not found")
	self.send_header("Content-Length", "0")
	self.send_header()

def bad_endpoint(self, path, params, kind):
	"""
	Handle a bad endpoint being called on
	"""
	
	t = Template("error.template")
	t.addVariable("error", f"<h1>400 Bad request</h1><p>We had a problem processing your request.</p><p><i>Endpoint: {path[0]}</i></p><p><i>Parameters: {params}</i></p>", sanitise = False)
	msg = t.evaluate()
	
	self.send_response(400, 'Bad request')
	self.send_header("Content-Length", str(len(msg)))
	self.send_header("Content-Type", "text/html")
	self.end_headers()
	
	if (kind == "HEAD"):
		return
	
	self.wfile.write(msg)

def home(self, path, params, kind):
	"""
	Temp home page
	"""
	
	t = Template("error.template")
	t.addVariable("error", f"<h1>Welcome to yuBe!</h1><p>Many of our pages like home, videos, recent and popular aren't ready yet!</p><p>Click here for sample video:<br/><a href=\"http://localhost:8000/watch?video=PROkfP3tpXrQrth_uZ0NQM0u\">http://localhost:8000/watch?video=PROkfP3tpXrQrth_uZ0NQM0u</a></p>", sanitise = False)
	msg = t.evaluate()
	
	self.send_response(200, 'OK')
	self.send_header("Content-Length", str(len(msg)))
	self.send_header("Content-Type", "text/html")
	self.end_headers()
	
	if (kind == "HEAD"):
		return
	
	self.wfile.write(msg)

def get_site_resource(self, path, params, kind):
	"""
	Send a resource from the table of allowed resources
	"""
	
	# The allowed resources table
	resource_table = {
		"style.css": ["style/style.css", "text/css"],
		"m3.css": ["style/m3.css", "text/css"],
		"player.js": ["script/player.js", "text/javascript"],
		"login.js": ["script/login.js", "text/javascript"],
		"videometa.js": ["script/videometa.js", "text/javascript"],
		"icon.svg": ["assets/favicon.svg", "image/svg+xml"],
		"icon.png": ["assets/favicon.png", "image/png"],
		"pause.svg": ["assets/pause.svg", "image/svg+xml"],
		"play.svg": ["assets/play.svg", "image/svg+xml"],
		"logo.svg": ["assets/logo.svg", "image/svg+xml"],
	}
	
	try:
		# Load requested resource, we can trust the path.
		data = files.loadFile(resource_table[path[1]][0], False, sanitise = False)
		
		self.send_response(200, "OK")
		self.send_header("Content-Length", str(len(data)))
		self.send_header("Content-Type", resource_table[path[1]][1])
		self.end_headers()
		
		if (kind == "HEAD"):
			return
		
		self.wfile.write(data)
	
	except FileNotFoundError:
		# File was not found ...
		not_found(self, path, params)
