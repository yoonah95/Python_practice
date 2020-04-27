

import StringIO

s = '''
Python is a cool little language,
It is well designed,compact,easy to learn and fun to program in.
Python strongly
'''


f = StringIO.StringIO(s)
print(f.read().upper())


