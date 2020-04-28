

import anydbm

f = anydbm.open('music','c')

f['flute'] = 'wood wind'
f['violin'] = 'string'
f['piano'] = 'keyboard'
print(f.keys())
print(f.values())
print(f.items())
print(len(f))
print(f['flute'])
print(f['violin'])
f.close()
