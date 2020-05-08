import threading

from queue import Queue

def creator(data,q):

	print('Creating data and putting it on the queue')
	print('\n')
	for item in data:
		evt = threading.Event()
		q.put((item,evt))
		print('Waiting for data to be doubled')
		evt.wait()


def consumer(q):

	while True:
		data,evt = q.get()
		print('Receive Original Data: {}',format(data))
		processed = data*5
		print('Receive Processed Data:{}',format(processed))
		print('\n')
		evt.set()
		q.task_done()


if __name__ == '__main__':
	q = Queue()
	data = [7,14,34,12,65,75]
	thread_one = threading.Thread(target=creator,args=(data,q))
	thread_two = threading.Thread(target=consumer,args=(q,))
	thread_one.start()
	thread_two.start()


	q.join()

