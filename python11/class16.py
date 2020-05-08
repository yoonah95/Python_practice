




class New(object):
	def __getattribute__(self,x):
		print('getattribute called..',x)
		return object.__getattribute__(self,x)


n = New()
n.x = 1
print(n.x)
print(n.y)


