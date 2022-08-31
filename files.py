import json
import os

def sanitisePath(unsafe_path):
	"""
	Sanitise a file path by removing any harmful or erronious chars
	"""
	
	ALLOWED_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_."
	new_path = ""
	
	for c in unsafe_path:
		if (c in ALLOWED_CHARS):
			new_path += c
	
	return new_path

def loadJson(path, *, sanitise = True):
	"""
	Load a json file, returning the contents or none if it does not exist
	"""
	
	path = sanitisePath(path) if sanitise else path
	
	content = ""
	
	try:
		with open(path, "r") as f:
			content = json.load(f)
	except FileNotFoundError:
		return None
	
	return content

def saveJson(path, content, *, sanitise = True):
	"""
	Save a json file
	"""
	
	path = sanitisePath(path) if sanitise else path
	
	with open(path, "w") as f:
		json.dump(content, f)

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

def file_length(path, *, sanitise = True):
	"""
	Get the size of the file at path
	"""
	
	path = sanitisePath(path) if sanitise else path
	
	# get file size
	return os.path.getsize(path)

def file_read_part(path, start, end, *, sanitise = True):
	"""
	Read part of a file's contents. Only intended for binary files
	"""
	
	path = sanitisePath(path) if sanitise else path
	
	# Get end if None
	if (end == None):
		end = file_length(path, sanitise = False) # Already sanitised if that is wanted
	
	# Find length to read
	length = end - start
	
	# Read content
	f = open(path, "rb")
	f.seek(start)
	c = f.read(length)
	f.close()
	
	return c

def file_append(path, content, encode = False, *, sanitise = True):
	"""
	Append more content to the end of a file, optionally encoding it
	"""
	
	path = sanitisePath(path) if sanitise else path
	f = open(path, "a") if encode else open(path, "ab")
	c = content.encode('utf-8') if encode else c
	f.write(c)
	f.close()

def create_folder(path, *, sanitise = True):
	"""
	Create a folder, including any folders needed to create that folder
	"""
	
	path = sanitisePath(path) if sanitise else path
	
	os.makedirs(path, exist_ok = True)

def delete(path, *, sanitise = True):
	"""
	Delete a file
	"""
	
	path = sanitisePath(path) if sanitise else path
	
	os.remove(path)
