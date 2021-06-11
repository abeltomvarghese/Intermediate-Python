if __name__ == '__main__':

	add10 = lambda x: x + 10
	print(add10(15))

	mult = lambda x, y: x * y
	print(mult(2,7))

	points2D = [(1,2), (15,1), (7,3), (3,4)]
	sortedCoord = sorted(points2D)
	print(sortedCoord)

	sortedYCoord = sorted(points2D, key=lambda x: x[1])
	print(sortedYCoord)

	sortedBySum = sorted(points2D, key=lambda x: x[0] + x[1])
	print(sortedBySum)

	a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	b = map(lambda x: x**2 ,a)
	print(list(b))

	c = [x**2 for x in range(11)] #ALTERNATIVE: [x**2 for x in a]
	print(c)

