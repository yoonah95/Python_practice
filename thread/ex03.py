




import threading
import queue


class _Operation(threading.Thread):
	def __init__(self,sem,*args,**kwds):
		self.sem = sem
		self.method = kwds.pop('target')
		super().__init__(targer=self.wrappedTarget , args=args,kwds=kwds,daemon=True)

	def wrappedTarget(self,*args,**kwds):
		self.method()
		if isinstance(self.sem,threading.Semaphore):
			self.sem.release()

class OperationQueue:
	def __init__(self,numberOfConcurrentTask=1):
		self.queue = queue.Queue()
		self.sem = threading.Semaphore(numberOfConcurrentTask)

	def add(self,method,*args,**kwds):
		task = _Operation(self.sem,method,*args,**kwds)
		self.queue.put(task)


	def mainloop(self):
		while True:
			t = self.queue.get()
			self.sem.acquire()
			t.start()

	def start(self,run_async=False):
		t = threading.Thread(target=self.mainloop,daemon=True)
		t.start()
		if not run_async:
			t.join()


def foo(n):
	for i in range(n):
		print(i)
		time.sleep(0.25)


q = OperationQueue(3)

q.start(True)

for _ in range(100):
	q.add(foo,random.randrange(2,40))


time.sleep(40)


















