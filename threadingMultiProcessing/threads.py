from threading import Thread
import os
from queue import Queue
def returnName(name):
	print(name)


if __name__ == '__main__':
	numThreads = os.cpu_count()
	threads = []

	for i in range(numThreads):
		t = Thread(target=returnName, args=("Bruce Wayne",))
		threads.append(t)

	for t in threads:
		t.start()

	for t in threads:
		t.join()

