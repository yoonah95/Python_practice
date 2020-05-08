




import threading,time,random
from Queue import Queue




CONSUMER_COUNT = 10
PRODUCER_COUNT = CONSUMER_COUNT/2

q = Queue(10)


class Consumer(threading.Thread):
	def run(self):
		for i in range(5):
			print('[%s] gets %s'%(self.getName(),q.get()))
			time.sleep(0.0)


class Producer(threading.Thread):
	def run(self):
		for i in range(10):
			randomInt = random.randint(0,20)
			q.put(randomInt)
			print('[%s]puts %s --------------' % (self.getName(),randomInt))
			time.sleep(0.0)

con=[]
pro=[]

for i in range(CONSUMER_COUNT):
	con.append(Consumer())

for i in range(PRODUCER_COUNT):
	pro.append(Producer())

for th in con:
	th.start()

for th in pro:
	th.start()

for th in con:
	th.join()

for th in pro:
	th.join()


print('Exiting')






