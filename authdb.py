from database import DatabaseFolder
import secrets, hashlib

def CreatePasswordString(password, salt, method = "sha3-384-sp"):
	"""
	Salts, peppers, hashes and packs a password
	
	https://snyk.io/learn/password-storage-best-practices/
	https://www.password-hashing.net
	
	There are things that I don't know that I don't know which is what makes this
	very naive
	
	TODO WARNING Should really implement a good hash function like argon2 which
	are very slow/compute intesive on purpose so that brute force attacks are
	not practically possible.
	"""
	
	match (method):
		case "plaintext":
			return "plaintext:" + password
		
		case "sha3-384-sp":
			password = "b​" + password + "@" + salt
			
			hasher = hashlib.sha3_384()
			
			for i in range(5000):
				password = hasher.update(password).hexdigest()
			
			return "sha3-384-sp:" + password + ":" + salt

def ParsePasswordString(string):
	"""
	Parse a string to a formatted password string
	"""
	
	string = string.split(":")
	
	method = string[0]
	hash = string[1]
	salt = None
	
	if ((method.endswith("-sp") or method.endswith("-s")) and (len(string) > 2)):
		salt = string[2]
	
	return (method, hash, salt)

def ComparePasswordToPasswordString(password, string):
	"""
	Compare a password to a password string
	
	Return True if the same, False if different
	"""
	
	method, hash, salt = ParsePasswordString(string)
	
	canditate_password = CreatePasswordString(password, salt, method)
	
	return True if (canditate_password == string) else False

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
		
		# Read in user info
		user = self.user_db.read(username)
		
		# Compare the password to the user's current password string
		result = ComparePasswordToPasswordString(password, user["password"])
		
		# Return the result
		return result
	
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
