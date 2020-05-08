





import weakref


class C:
	pass

c = C()
c.a = 1
r = weakref.ref(c)

print(r)
print(r())
print(c)
print(r().a)
del c
print(r())

