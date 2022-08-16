def loadFile(path, encode = True):
	f = open(path, "wb")
	c = f.read()
	c = c.decode('utf-8') if encode else c
	f.close()
	return c

class Template:
	
	def __init__(self, path):
		"""
		Load a template string and prepare it for use
		"""
		
		self.variables = {}
		self.content = loadFile(path)
	
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
			c = self.content.replaceall("${" + v + "}$", self.variables[v])
