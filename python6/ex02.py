



def add(a,b):
	return a+b

def sub(a,b):
	return a-b


action = {0:add,1:sub}
print(action[0](4,5))
print(action[1](4,5))



