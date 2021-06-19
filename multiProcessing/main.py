from multiprocessing import Process, Queue, Array, Lock

def addHundred(sharedArr, lock):
	for x in range(100):
		with lock:
			for i in range(len(sharedArr)):
				sharedArr[i] += 1

def add10(nums, queue):
	for i in nums:
		queue.put(i + 10)

def minus10(nums, queue):
	for i in nums:
		queue.put(i - 10)


if __name__ == '__main__':
	lock = Lock()

	sharedArr = Array('d',[0.0, 100.0, 200.0, 300.0])
	print("Beginning Array: ", sharedArr[:])

	p1 = Process(target=addHundred, args=(sharedArr, lock))
	p2 = Process(target=addHundred, args=(sharedArr, lock))

	p1.start()
	p2.start()

	p1.join()
	p2.join()

	print("End Array: ", sharedArr[:])

	#WITH QUEUES
	q = Queue()
	nums = range(1,6)

	p3 = Process(target=add10, args=(nums,q))
	p4 = Process(target=minus10, args=(nums, q))

	p3.start()
	p4.start()

	p3.join()
	p4.join()

	while not q.empty():
		print(q.get())