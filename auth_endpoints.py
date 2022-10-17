"""
TODO: CSRF, proper password storage(!), lookup common security holes that others
might try to take advantage of!
"""
from template import Template
import json

MAX_STRING_SIZE = 5120

ERROR_STATUS_STRING = {
	400: "Bad request",
	401: "Unauthorised",
	402: "Payment required",
	403: "Forbidden",
	404: "File not found",
	405: "Method not allowed",
	411: "Length required",
	413: "Payload too large",
	425: "Too early",
	451: "Unavailable for legal reasons",
	500: "Interal server error",
	503: "Service unavailable",
	600: "Stop drinking",
}

def error(self, number):
	"""
	Send an 4xx or 5xx error
	"""
	
	self.send_response(number, ERROR_STATUS_STRING[number])
	self.send_header("Content-Length", "0")
	self.send_header()

def load_post_data(self, path, params, kind):
	"""
	Load data from a POST request
	"""
	
	# GET doesn't make sense
	if (kind == "GET" or kind == "HEAD"):
		error(self, 405)
		return
	
	# Get content length
	if (self.headers.get("Content-Length", None) == None):
		error(self, 411)
		return
	
	content_length = int(self.headers["Content-Length"])
	
	# Check if content is too long or too short
	if (content_length == 0 and content_legnth > MAX_STRING_SIZE):
		error(self, 413)
		return
	
	# Read in the data
	data = self.rfile.read(content_legnth)
	
	# Decode the bytes to a string
	data = data.decode("utf-8")
	
	# Return loaded JSON string
	try:
		return json.loads(data)
	except:
		return {}

def login(self, path, params, kind):
	"""
	Log a user into YuBe
	"""
	
	# Load request data
	info = load_post_data(self, path, params, kind)
	
	# Handle some errors
	if (info == None):
		return
	
	print(info)
	
	# Get username and password requested used
	username = info.get("username", None)
	password = info.get("password", None)
	
	# Get requested action types
	permissions = info.get("permissions", None)
	
	if (not username or not password or not permissions):
		return error(self, 400)
	
	# TODO: You need to implement authdb first :)
	db = authdb.AuthDB()
	
	token = db.generateToken(username, password, permissions)
	
	if (not token):
		return error(self, 403)
