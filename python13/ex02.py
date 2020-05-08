



class C:
	pass

c = C()
c.a = 2
print(c.a)
p = weakref.proxy(c)
print(p)

print(p.a)

r = weakref.ref(c)
p = weakref.proxy(c)


print(weakref.getweakrefcount(c))

print(weakref.getweakrefs(c))


