





class Person:
	def __init(self,name,phone = None):
		self.name = name
		self.phone = phone
	
	def __repr__(self):
		return '<Person %s %s>' % (self.name,self.phone)

class Employee(Person):
	def __init__(self,name,phone,position,salary):
		Person.__init__(self,name,phone)
		self.position = position
		self.salary = salary

p1 = Person('gslee',5284)

