



s = """
Its power: Python developers typically report \
they are able to deveop 
"""

f = file('t.txt','w')
f.write(s)
f.close()

f = file('t.txt')
s = f.read()
print(s)

