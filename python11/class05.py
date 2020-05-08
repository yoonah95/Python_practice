



class MyString:
	def __init__(self,str):
		self.str = str

	def __div__(self,sep):
		return self.str.split(sep)




