import json

def sanitisePath(unsafe_path):
	"""
	Sanitise a file path by removing any harmful or erronious chars
	"""
	
	ALLOWED_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_."
	new_path = ""
	
	for c in unsafe_path:
		if (c in ALLOWED_CHARS):
			new_path += c
	
	return new_path

def loadJson(path, *, sanitise = True):
	"""
	Load a json file
	"""
	
	path = sanitisePath(path) if sanitise else path
	
	content = ""
	
	with open(path, "r") as f:
		content = json.load(f)
	
	return content

def loadFile(path, decode = True, *, sanitise = True):
	"""
	Load file contents, optionally decoding it
	"""
	
	path = sanitisePath(path) if sanitise else path
	f = open(path, "rb")
	c = f.read()
	c = c.decode('utf-8') if decode else c
	f.close()
	return c

