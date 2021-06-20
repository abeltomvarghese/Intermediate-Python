
if __name__ == '__main__':
	nums = range(1,11)
	*firstSet, lastNum = nums
	print("first set", firstSet)
	print("last num", lastNum)

	print("")
	beginning, *middle, end = nums
	print("beginning:", beginning)
	print("middle:", middle)
	print("end:", end)


	oddNums = list(range(1,11,2))
	evenNums = tuple(range(0,11,2))

	allNums = [*oddNums, *evenNums]
	nums = sorted(allNums)
	print(nums)

	# WITH DICTIONARIES
	firstDic = {'a': 1, 'b':2}
	secondDic = {'c':3, 'd':4, 'e':5}

	myDict = {**firstDic, **secondDic}
	print(myDict)

