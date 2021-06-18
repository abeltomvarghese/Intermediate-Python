from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
from itertools import groupby
from itertools import count, cycle, repeat
import operator


def smaller_than_3(x):
	return x < 3


if __name__ == '__main__':
	a = [1, 2]
	b = [3, 4]
	prod = product(a, b)  # product(a,b,repeat=2)
	print("PRODUCT: " + str(list(prod)))

	c = [1, 2, 3, 4, 5]
	perm = permutations(c, 2)
	print("PERMUTATION: " + str(list(perm)))

	d = [1, 2, 3, 4, 5]
	comb = combinations(d, 2)
	print("COMBINATION: " + str(list(comb)))

	comb_wr = combinations_with_replacement(d, 2)
	print("COMB + WR: " + str(list(comb_wr)))

	print("WITHOUT ACCUMULATION: " + str(list(d)))
	acc = accumulate(d)
	print("ACCUMULATION: " + str(list(acc)))

	acc = accumulate(d, func=operator.mul)
	print("MULTIPLIED ACCUMULATION: " + str(list(acc)))

	e = [1, 3, 2, 4, 7, 6, 5]
	acc = accumulate(e, func=max)
	print("MAX ACCUMULATION: " + str(list(acc)))

	group_obj = groupby(c, smaller_than_3)

	for key, value in group_obj:
		print(key, list(value))

	# same thing but with lambda

	l_group_obj = groupby(c, lambda x: x < 3)

	for key, value in l_group_obj:
		print(key, list(value))

	garage = [{'name': 'Mercedes', 'topSpeed': 155}, {'name': 'Rolls Royce', 'topSpeed': 155},
			  {'name': 'Range Rover', 'topSpeed': 140},
			  {'name': 'Lamborghini', 'topSpeed': 217}, {'name': 'LaFerrari', 'topSpeed': 217},
			  {'name': 'SLR Mclaren', 'topSpeed': 217},
			  {'name': 'Bugatti', 'topSpeed': 261}, {'name': 'Land Rover', 'topSpeed': 80}]

	groupGarage = groupby(garage, lambda x: x['topSpeed'])

	for key, value in groupGarage:
		print(key, list(value))

	#infinite cycles
	# for i in count(5):
	# 	print(i)
	# 	if i == 5:
	# 		break
	#
	# for x in cycle(c):
	# 	print(x)
	#
	for t in repeat(1,4): #prints out 1, four times
		print(t)

