#!/usr/bin/env python
"""
yu.be server
"""

import os, sys
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer

# TODO: Make loading endpoints a config option and allow dynamic loading of
# endpoints.
import site_endpoints
import video_endpoints
import auth_endpoints

YU_ENDPOINTS = {
	"bad-endpoint": site_endpoints.bad_endpoint,
	"": site_endpoints.home,
	"home": site_endpoints.home,
	"videos": site_endpoints.home,
	"recent": site_endpoints.home,
	"popular": site_endpoints.home,
	"get-resource": site_endpoints.get_site_resource,
	"watch": video_endpoints.watch,
	"get-video-data": video_endpoints.get_video_data,
	"login": auth_endpoints.login,
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
		Handle a GET request
		"""
		
		path, params = parsePath(self.path)
		
		endpoint = path[0]
		
		# Handle the request
		(YU_ENDPOINTS.get(endpoint, YU_ENDPOINTS["bad-endpoint"]))(self, path, params, "GET")
	
	def do_HEAD(self):
		"""
		Handle a HEAD request
		"""
		
		path, params = parsePath(self.path)
		
		endpoint = path[0]
		
		# Handle the request
		(YU_ENDPOINTS.get(endpoint, YU_ENDPOINTS["bad-endpoint"]))(self, path, params, "HEAD")
	
	def do_POST(self):
		"""
		Handle a POST request
		"""
		
		path, params = parsePath(self.path)
		
		endpoint = path[0]
		
		# Handle the request
		(YU_ENDPOINTS.get(endpoint, YU_ENDPOINTS["bad-endpoint"]))(self, path, params, "POST")

def main():
	server = ThreadingHTTPServer(('0.0.0.0', 8000), YuHandler)
	
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		return 0
	
	return 1

if (__name__ == "__main__"):
	sys.exit(main())
