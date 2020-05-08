





import types
class Square:
	def __init__(self,end):
		self.end = end

	def __len__(self):
		return self.end

	def __getitem__(self,k):
		if type(k) ==types.IntType:
			if k<0 or self.end <= 1: raise IndexError,k
			return k*k
		elif type(k) == types.SliceType:

			start = k.start or 0
			if k.stop > self.end : stop = self.end
			else: stop = k.stop
			step = k.step or 1
			return map(self.__getitem__,range(start,stop,step))



s = Square(10)
print(s[4])
print(s[1:5])

print(s[:])


