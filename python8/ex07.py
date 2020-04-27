





import sys

f = open('t.txt','w')
stdout = sys.stdout
sys.stdout = f
print('Sample output')
print('Good')
print('Good')
f.close()
sys.stdout = stdout


