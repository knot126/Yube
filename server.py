#!/usr/bin/env python
"""
yu.be server
"""

import os, sys
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer

import site_endpoints
import video_endpoints

YU_ENDPOINTS = {
	"bad-endpoint": site_endpoints.bad_endpoint,
	"get-resource": site_endpoints.get_site_resource,
	"watch": video_endpoints.watch,
}

def parsePath(path):
	"""
	Parse the URL path into (real_path, params)
	"""
	
	# Parse file paths and parameters
	# For example: /get-video-file/part?video=8frTtoQ46HXDJNEe&player=short
	# Result: path = ["get-video-file", "part"], params = {"video": "8frTtoQ46HXDJNEe", "player": "short"}
	
	# Remove leading '/'
	path = path[1:]
	
	# Split into path/params
	left_and_right = path.split("?")
	
	# Check if URI has any parameters
	has_params = (len(left_and_right) >= 2)
	
	# Init path/params final variables
	path = left_and_right[0]
	params = None
	
	# Parse parameters
	if (has_params):
		tmpparams = {}
		params = left_and_right[1].split("&")
		
		# Parse params
		for p in params:
			key, value = p.split("=")
			tmpparams[key] = value.replace("/", "&#47;") # NOTE: '/' could be problematic and should not be used so we filter it here
		
		params = tmpparams
		del tmpparams
	
	path = path.split("/")
	
	#print("server.parsePath", path, params)
	
	return (path, params)

class YuHandler(BaseHTTPRequestHandler):
	"""
	YuBe request handler
	"""
	
	def do_GET(self):
		"""
		Handle a get request
		"""
		
		path, params = parsePath(self.path)
		
		endpoint = path[0]
		
		# Handle the request
		if (endpoint in YU_ENDPOINTS):
			YU_ENDPOINTS[endpoint](self, path, params)
		else:
			# Redirect to bad-endpoint if endpoint is not valid
			YU_ENDPOINTS['bad-endpoint'](self, path, params)

def main():
	server = ThreadingHTTPServer(('0.0.0.0', 8000), YuHandler)
	
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		return 0
	
	return 1

if (__name__ == "__main__"):
	sys.exit(main())
