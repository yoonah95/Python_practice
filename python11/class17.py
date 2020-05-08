





class Accumulator:
	def __init__(self):
		self.sum = 0
	def __call__(self,*args):
		self.sum +=sum(args)
		return self.sum

acc = Accumulator()
print(acc(1,2,3,4,5))
print(acc(6))
print(acc(7,8,9))
print(acc.sum)



