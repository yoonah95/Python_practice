



class MyDict:
	def __init__(self,d=None):
		if d == None : d={}
		self.d =d

	def __getitem__(self,k):
		return self.d[k]
	def __setitem__(self,k,v):
		self.d[k] = v

	def __len__(self):
		return len(self.d)

	def keys(self):
		return self.d.keys()

	def values(self):
		return self.d.values()

	def items(self):
		return self.d.items()

m = MyDict({'one':1,'two':2,'three':3})
print(m.keys())
print(m.values())
print(m.items())


