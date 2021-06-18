import sys

def fibonacciSeq(limit):
	a,b = 0, 1
	while a < limit:
		yield a
		a, b = b, a + b


def firstNgenerator(n):
	num = 0
	while num < n:
		yield num
		num += 1

def firstnsum(n):
	num = 0
	nums = []
	while num < n:
		nums.append(num)
		num += 1
	return nums

def countdown(num):
	while num > 0:
		yield num
		num -= 1


def myGenerator():
	yield 1
	yield 2
	yield 3
	yield 54
	yield 4
	yield 5
	yield 6
	yield 7
	yield 8

if __name__ == '__main__':

	g = myGenerator()
	k = myGenerator()
	s = myGenerator()

	print(sum(k))

	for i in g:
		print(i)

	print(sorted(s))

	q = countdown(10)

	for index in (q):
		print(index)

	print(sum(firstNgenerator(100)))
	print(sys.getsizeof(firstNgenerator(100)))

	print(sys.getsizeof(firstnsum(100)))

	fib = fibonacciSeq(100)
	for i in fib:
		print(i)


	#Generator Generation

	newGenerator = (i for i in range(10000000) if i % 2 == 0)
	newList = [i for i in range(10000000) if i % 2 == 0]

	# for i in newGenerator:
	# 	print(i)

	print("size of generator object " + str(sys.getsizeof(newGenerator)))
	print("size of normal list " + str(sys.getsizeof(newList)))

	convertedList = list(newGenerator)
	print("size of converted list from generator " + str(sys.getsizeof(convertedList)))