#-*-coding:utf-8-*-




class Person:
	def __init__(self,name,phone=None):
		self.name = name
		self.phone = phone
	def display(self):
		return '<Person %s %s>' % (self.name, self.phone)


class Employee(Person):
	def __init__(self,name,phone,position,salary):
		Person.__init__(self,name,phone)
		self.position = position
		self.salary = salary

m1 = Employee('손창희',5564,'대리',200)

print(m1.name,m1.position)
