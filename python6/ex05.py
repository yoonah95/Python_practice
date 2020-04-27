







d ={ 'one':1,'two':2,'three':3}
L = d.items()
L.sort()

print(L)

L.sort(key=lambda item:item[1])

print(L)


