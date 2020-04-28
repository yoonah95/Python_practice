



import pickle

phone = {'tom' :4358382 , 'jack':9465215,'jim':6851325,'Joseph':6584321}
List = ['string',1234,0.2345]
Tuple = (phone,List)

f = open('t2.txt','w')

pickle.dump(Tuple,f)
f.close()

f = open('t2.txt')
x,y = pickle.load(f)
print(x)
print(y)


