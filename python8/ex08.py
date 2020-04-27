




import sys
import StringIO

stdout = sys.stdout
sys.stdout = f = StringIO.StringIO()

print('Sample output')
print('good')
print('Good')

sys.stdout = stdout 
s = f.getvalue()

print 'Done-------------'
print(s)


