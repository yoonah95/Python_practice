



class Wrapper:
	def __init__(self,data):
		self.data = data

	def __repr__(self):
		return `self.data`

	def __str__(self):
		return str(self.data)

	def get(self):
		return self.data

	def __getattr__(self,attrname):
		return getattr(self.data,attrname)

wComplex = Wrapper(5+3j)
print(wComplex.imag)

