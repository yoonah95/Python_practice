











f = open('removeme.txt','w')
f.write('firsr line\n')
f.write('second line\n')
f.close()


f = open('removeme.txt','a')
f.write('third line\n')
f.close()

f = open('removeme.txt')
print(f.read())



