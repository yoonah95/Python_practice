


class Animal:
	def cry(self):
		print('...')


class Dog(Animal):
	def cry(self):
		print('wall wall')

class Fish(Animal):
	pass

class Duck(Animal):
	def cry(self):
		print('dudu')

for each in (Dog(),Duck(),Fish()):
	each.cry()


