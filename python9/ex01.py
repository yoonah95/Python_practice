





def addmember(memberlist,newmembers):
if type(newmembers) not in (type([]),type(())):
	newmembers = [newmembers]

	for m in newmembers:
		if m not in memberlist:
			memberlist.append(m)

