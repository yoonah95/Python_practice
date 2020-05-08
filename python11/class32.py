




class MyList(list):
	def __sub__(self,other):
		L=self[:]
		for x in other:
			if x in L : L.remove(x)
		return L

L = MyList([1,2,3,'spam',4,5])
L = L -['spam']
print(L)


