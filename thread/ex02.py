




import threading,Queue
import time


class Catcher(threading.Thread):
	def __init__(self,id,dataQueue):
		threading.Thread.__init__(self)
		self.id = id
		self.dataQueue = dataQueue


	def run(self):
		while True:
			data = self.dataQueue.get()

			print("["+str(self.id)+":"+str(data)+"]")
			self.dataQueue.task_done()


def main():


	StringQueue = Queue.Queue()
	StringQueue.put(1)
	StringQueue.put(2)

	cat1 = Catcher("A",StringQueue)
	cat1.setDaemon(True)


	cat2 = Catcher("B",StringQueue)
	cat2.setDaemon(True)

	cat1.start()
	cat2.start()

	StringQueue.put(3)
	StringQueue.put(4)

	cat1.dataQueue.join()
	cat2.dataQueue.join()


if __name__=="__main__":
	main()


