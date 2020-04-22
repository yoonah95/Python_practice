

L = [(i,j,i*j) for i in range(2,100,2) for j in range(3,100,3) if(i+j) %7==0]
print(L)

