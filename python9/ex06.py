








func = [lambda x,y:x+y , lambda x,y:x-y , lambda x,y:x*y,lambda x,y:x/y]


def menu():
	print("0. add")
	print("1.sub")
	print("2.mul")
	print("3.div")
	print("4.quit")
	return input('Select menu:')




while 1:
	sel = menu()
	if sel < 0 or sel > len(func):
		continue
	if sel == len(func):
		break
	x = input('First operand:')
	y = input('Second operand:')
	print('Result=',func[sel](x,y))


