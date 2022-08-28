import files

class Template:
	
	def __init__(self, path):
		"""
		Load a template string and prepare it for use. Path should never be taken
		from the user.
		"""
		
		self.variables = {}
		self.content = files.loadFile(path, sanitise = False)
	
	def addVariable(self, variable, value):
		"""
		Add a variable to the template
		"""
		
		self.variables[variable] = value
	
	def evaluate(self):
		"""
		Evaluate the template into real content
		"""
		
		c = self.content
		
		for v in self.variables.keys():
			c = c.replace("${" + v + "}$", self.variables[v])
		
		return c.encode('utf-8')
