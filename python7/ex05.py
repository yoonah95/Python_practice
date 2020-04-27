





octtab = {'0':'000' , '1':'001' , '2':'010' , '3':'011' , '4':'100' , '5':'101' ,'6':'110' , '7':'111'}

def bin1(d,width=0):
	"integer to binary(string)"
	s="%o" % d
	b=''
	for el in s :
		b+=octtab[el]
	if width > 0 :
		if len(s) > width:
			return b[:width]
		b=b.zfill(width)
	return b

print(bin1(23,7))


