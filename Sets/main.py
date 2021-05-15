if __name__ == '__main__':
	mySet = {1,2,3,4,5}
	print(mySet)

	print(type(mySet))

	nbaTeams = set()

	nbaTeams.add("Chicago Bulls")
	nbaTeams.add("Los Angeles Lakers")
	nbaTeams.add("Golden State Warriors")
	nbaTeams.add("Memphis Grizzlies")
	nbaTeams.add("New Orleans Pelicans")
	nbaTeams.add("New York Knicks")
	nbaTeams.add("Detroit Pistons")
	nbaTeams.add("San Antonio Spurs")
	nbaTeams.add("LA Clippers")
	nbaTeams.add("Washington Wizards")
	nbaTeams.add("Miami Heat")

	nbaTeams.add("New England Patriots")
	nbaTeams.discard("New England Patriots") #safer alternative to remove method as it doesn't throw an error

	for team in nbaTeams:
		print(team)

	if "New York Knicks" in nbaTeams:
		print("knicks rule")


	odds = {1,3,5,7,9}
	even = {0,2,4,6,8,10}
	primes = {2,3,5,7}

	union = odds.union(even)
	print(union)

	intersection = odds.intersection(primes)
	print(intersection)

	setA = {1,2,3,4,5,6,7,8,9,10,11,12}
	setB = {1,2,3,5,8,10}

	diff = setA.difference(setB)
	print(diff)

	setA.update(setB)
	print(setA)

	setA.intersection_update(setB)
	print(setA)

	setA.difference_update(setB)
	print(setA)

	setA.symmetric_difference_update(setB)
	print(setA)

	setC = {1,2,3,4}
	setD = {1,2,3,4,5,6,7,8}

	print(setC.issubset(setD))
	print(setD.issuperset(setC))

	mercedesRange = frozenset(["A-Class","B-Class","C-Class","E-Class","G-Class","M-Class","S-Class","V-Class"])

	print(mercedesRange)
