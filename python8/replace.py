



import sys
import re



def replace(fname,srcstr,deststr):
	f= open(fname)
	txt = f.read()
	txt = re.subn(srcstr,deststr,txt)[0]
	return txt

if __name__ == '__main__':
	if len(sys.argv) != 4:
		print("""Usage : replace filename srcstr desff""")
		sys.exit()

	print(replace(sys.argv[1],sys.argv[2],sys.argv[3])



