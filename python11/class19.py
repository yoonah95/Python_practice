




class D(object):
	

	def __init__(self):
		self.__degree = 0

	def get_degree(self):
		return self.__degree
	def set_degree(self,d):
		self.__degree = d%360
	
	degree = property(get_degree,set_degree)



d = D()
d.degree = 10
print(d.degree)

d.degree = 370
print(d.degree)

d.degree = -370
print(d.degree)


