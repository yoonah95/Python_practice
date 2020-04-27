


def add(a,b):
	return a+b

def sub(a,b):
	return a-b

def mul(a,b):
	return a*b

def div(a,b):
	return a/b

def choose_menu():
	print ('What do you want to do?')
	print ('add,sub,mul,div,guit')
	return input('Your choice :')

menu ={'add':add , 'sub':sub,'mul':mul,'div':div}
choice = choose_menu()
while choice != 'quit':
	if choice in menu:
		print("Zz")
		x=input('first value :')
		y=input('second value:')
		print(x)
		print(y)	
	
		print(menu[choice](x,y))
	choice=choose_menu()




