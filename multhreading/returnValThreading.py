from queue import Queue
import os
from threading import Thread, Lock

identities = ['Steve Rogers', 'Natasha Romanoff', 'Tony Stark', 'Thor Odinson', 'Peter Parker', 'Bucky Barnes', 'King T\'challa',
			  'Bruce Wayne', 'Stan Lee', 'Barry Allen', 'Arthur Curry', 'Diana Prince']

def exposeHeros():
	global identities
	if len(identities) > 0:
		with lock:
			id = identities.pop()
			return id


if __name__ == '__main__':
	que = Queue()
	cpuCount = os.cpu_count()

	threadList = []
	lock = Lock()

	for i in range(cpuCount):
		t = Thread(target=lambda q: q.put(exposeHeros()), args=(que,))
		t.daemon = True
		t.start()
		threadList.append(t)

	for t in threadList:
		t.join()

	while not que.empty():
		result = que.get()
		print(result)
