





def dosomething():
	a = 1/0


try:
	dosomething()

except ArithmeticError:
	print('Exception occured')


