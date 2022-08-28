import files

def sanitiseFromStringToHtml(string):
	"""
	Sanitise the strings:
	" -> &quot;
	< -> &lt;
	> -> &gt;
	& -> &amp;
	"""
	
	return string.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")

class Template:
	
	def __init__(self, path):
		"""
		Load a template string and prepare it for use. Path should never be taken
		from the user.
		"""
		
		self.variables = {}
		self.content = files.loadFile(path, sanitise = False)
	
	def addVariable(self, variable, value, sanitise = True):
		"""
		Add a variable to the template
		"""
		
		value = sanitiseFromStringToHtml(value) if sanitise else value
		
		self.variables[variable] = value
	
	def evaluate(self):
		"""
		Evaluate the template into real content
		"""
		
		c = self.content
		
		for v in self.variables.keys():
			c = c.replace("${" + v + "}$", self.variables[v])
		
		return c.encode('utf-8')
