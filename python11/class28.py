




class Base:
	def f(self):
		self.g()

	def g(self):
		print('Base')

class Derived(Base):
	def g(self):
		print('Derived')

b =Base()
b.f()

a = Derived()
a.f()
