from database import DatabaseFolder
import secrets

class AuthDB():
	"""
	Class which wraps around the authentication database and provides single
	implementations of helpful methods
	"""
	
	def __init__(self):
		"""
		Initialise authdb connections
		"""
		
		# Database for users
		self.user_db = DatabaseFolder("user")
		
		# Database for active sessions
		self.sessions_db = DatabaseFolder("session")
	
	def _authenticate(self, username, password):
		"""
		Check that the user's password and the challenge password are the same
		"""
		
		# WARNING TODO actually implement user passwords
		return True
	
	def generateToken(self, username, password, permissions):
		"""
		Generate a token for a user
		"""
		
		# Check the username and password
		# Note: using != True since this seems to be most resistant to code change
		# accidents
		if (self._authenticate(username, password) != True):
			return None
		
		# Read user info
		user = self.user_db.read(username)
		
		if (not user):
			return None
		
		# Random token ID
		token_id = secrets.token_urlsafe(128)
		
		# WARNING TODO Fix what happens when a token by the id already exists (very rare)
		
		# Add the token
		if ("sessions" in user):
			user["sessions"].append(token_id)
		else:
			user["sessions"] = [token_id]
		
		# Write new user file
		self.user_db.write(username, user)
		
		# Write token file
		self.sessions_db.write(token_id, {"token": token_id, "username": username, "permissions": permissions, "expire": None})
		
		# Return token id
		return token_id
	
	def validate(self, username, token, action):
		"""
		Validate that the user can perform the action with the specified token
		"""
		
		return False
