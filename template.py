import files

def formatFromStringToHtml(string):
	"""
	Properly formats a string for display. This must be done after sanitisation
	since it will add some html stuff.
	"""
	
	newstring = ""
	
	# Add padding to the string to support formatting better, this will also
	# make implementation easier and avoid lots of tests
	string = " " + string + " "
	
	# Parse bold, italic and code
	for i in range(1, len(string) - 1):
		match (string[i]):
			case '_':
				if (string[i - 1] == " " or string[i - 1] == "\n"):
					newstring += "<i>"
				elif (string[i + 1] == " " or string[i + 1] == "\n"):
					newstring += "</i>"
				else:
					newstring += string[i]
			case '*':
				if (string[i - 1] == " " or string[i - 1] == "\n"):
					newstring += "<b>"
				elif (string[i + 1] == " " or string[i + 1] == "\n"):
					newstring += "</b>"
				else:
					newstring += string[i]
			case '`':
				if (string[i - 1] == " " or string[i - 1] == "\n"):
					newstring += "<code>"
				elif (string[i + 1] == " " or string[i + 1] == "\n"):
					newstring += "</code>"
				else:
					newstring += string[i]
			case _:
				newstring += string[i]
	
	# Replace newlines and tabs with html escape versions
	newstring = newstring.replace("\n", "<br/>").replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;")
	
	return newstring

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
	
	def addFormattedVariable(self, variable, value):
		"""
		Add a formatted variable string. This is always user input or plain text
		so it must be sanitised
		"""
		
		self.variables[variable] = formatFromStringToHtml(sanitiseFromStringToHtml(value))
	
	def evaluate(self):
		"""
		Evaluate the template into real content
		"""
		
		c = self.content
		
		for v in self.variables.keys():
			c = c.replace("${" + v + "}$", self.variables[v])
		
		return c.encode('utf-8')
