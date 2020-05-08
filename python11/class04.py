





from time import time,ctime,sleep

class Life:
	def __init__(self):
		self.birth = ctime()
		print('Birthday',self.birth)
	def __del__(self):
		print('Deathday',ctime())


def test():
	mylife=Life()
	print('Sleeping for 3 sec')
	sleep(3)


test()



