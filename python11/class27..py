


class A:
	def save(self):
	print('A save called')

class B(A):
	pass

class C(A):
	def save(self):
		print('C save called')

class D(B,C):
	pass

d = D()
d.save()
