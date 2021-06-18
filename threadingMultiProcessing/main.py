import os
from multiprocessing import Process

def squareNums(limit):

	for i in range(limit):
		i * i


if __name__ == '__main__':
	processes = []
	numProcess = os.cpu_count()

	for i in range(numProcess):
		p = Process(target=squareNums, args=(100,))
		processes.append(p)

	for p in processes:
		p.start()

	for p in processes:
		p.join()

	print("All finished")