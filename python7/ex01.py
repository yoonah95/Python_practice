

import copy

a = [1,2,3]
b = [4,5,a]
x = [a,b, 100]
y = copy.copy(x)


print(y)


y = copy.deepcopy(x)

print(y)
