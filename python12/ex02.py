




class SquareSeq:
	def __init__(self,n):
		self.n = n

	def __getitem__(self,k):
		if k>= self.n or k<0:
			raise IndexError
		return k*k

	def __len__(self):
		return self.n


s = SquareSeq(10)
print(s[2],s[4])
for x in s:
	print(x),
print(s[20])



