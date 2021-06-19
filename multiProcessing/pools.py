from multiprocessing import Pool

def cube(num):
	return num ** 3

if __name__ == '__main__':

	nums = range(1,11)

	pool = Pool()
	#Available functions: map, apply, join, close
	result = pool.map(cube, nums)
	## result = pool.apply(cube, 10)
	pool.close()
	pool.join()

	print(result)