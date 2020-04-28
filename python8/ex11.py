


import anydbm
f = anydbm.open('music','c')
print(f.keys())

for k in f :
	print(k,f[k])


f['oboe'] = 'wood wind'
f['piano'] = 'keyboard instrument'
del f['violin']

for k in f:
	print(k,f[k])

f.close()
