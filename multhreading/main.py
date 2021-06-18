from threading import Thread, Lock

database_val = 0

def increase(lock):
	global database_val

	with lock:
		local_copy = database_val
		local_copy += 1
		database_val = local_copy


if __name__ == '__main__':
	threads = []

	lock = Lock()

	print("Start Value:", database_val)

	thread1 = Thread(target=increase, args=(lock,)).start()
	thread2 = Thread(target=increase, args=(lock,)).start()

	for i in threads:
		i.join()
		
	print("End Value: ", database_val)