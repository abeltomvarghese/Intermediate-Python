if __name__ == '__main__':
	shoppingList = ["Banana", "Cherry", "Apple"]
	print(shoppingList)

	weirdList = [5, True, "Apple", "Apple"]  # List can have multiple different data types & duplicate data
	print(weirdList)

	fruit = shoppingList[-2]  # -1 index corresponds to the last index in the list, -2 corresponds to the second to last item
	print(fruit)

	if "apple" in shoppingList:
		print("Apple included in list")
	else:
		print("not included")

	print("Length of shopping list: " + str(len(shoppingList)))

	shoppingList.append("Mango")
	shoppingList.insert(1, "Strawberry")

	for item in shoppingList:
		print("Item: " + item)

	bought = shoppingList.pop()  # removes the last item from the list
	print("Added to shopping cart: " + bought)

	shoppingList.remove("Cherry")

	shoppingList.clear()  # clears the entire list

	evenNums = [20, 2, 12, 8, 6, 18, 10]
	evenNums.sort()
	for nums in evenNums:
		print(nums)

	primeNums = [11, 13, 19, 1, 5, 3, 7]
	orderedPrimeNums = sorted(primeNums)  # sorts list & save to new variable, order of the original list maintained

	for oNums in orderedPrimeNums:
		print(oNums)

	myList = [0] * 5
	myList2 = [0,1,2,3,4,5]

	concatList = myList + myList2
	print(concatList)

	numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	subList = numList[1:5]
	subList2 = numList[:5] #starts from the beginning up to index 5
	sublist3 = numList[1:] #goes all the way to the end
	sublist4 = numList[1::2] #shows how the step function works in slicing
	sublist5 = numList[::-1] #reversing a list
	print(sublist5)

	lebron_james = ["Los Angeles Lakers", "Cleveland Cavaliers"]

	lebron = lebron_james #both lists point to the same location in memory

	lebron.append("Miami Heat")

	print(lebron_james)

	julian_edelman = ["New England Patriots"]

	tom_brady = julian_edelman.copy()  # this method ensures that the original list is preserved

	tom_brady.append("Tampa Bay Buccaneers")

	print(julian_edelman)
	print(tom_brady)

	squaredList = [i*i for i in numList] #list comprehension

	print(squaredList)