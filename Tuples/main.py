
if __name__ == '__main__':
	goat = ("Tom Brady", 12, "quarterback", 6, "New England Patriots")

	for attribute in goat:
		print(attribute)

	print(len(goat))
	print(goat.count(12))

	print(goat.index("New England Patriots"))

	goat_list = list(goat)
	print(type(goat_list))

	goat = tuple(goat_list)
	print(type(goat))

	team = goat[3:5] # tuple slicing
	print(team)

	# UNPACKING A TUPLE

	rookie = ("Ja Morant", 12, "Memphis Grizzlies")

	name,number,team = rookie

	print("Player name: " + name)
	print("Player number: " + str(number))
	print("Team: " + team)

	# Unpack multiple elements

	lebronJames = ("Cleveland Cavaliers", "Miami Heat", "Los Angeles Lakers")
	*previousTeams, currentTeam = lebronJames

	print(previousTeams)
	print(currentTeam)

	# measuring the size in bytes

	import sys

	nbaList = ["Chicago Bulls", "La Lakers", "Memphis Grizzlies", "Golden State Warriors", "Miami Heat", "New Orleans Pelicans"]
	nbaTuple = ("Chicago Bulls", "La Lakers", "Memphis Grizzlies", "Golden State Warriors", "Miami Heat", "New Orleans Pelicans")

	print(sys.getsizeof(nbaList),"bytes")
	print(sys.getsizeof(nbaTuple),"bytes")

	import timeit

	print(timeit.timeit(stmt="[\"Chicago Bulls\", \"La Lakers\", \"Memphis Grizzlies\", \"Golden State Warriors\", \"Miami Heat\", \"New Orleans Pelicans\"]"
						,number=100000000), "seconds")
	print(timeit.timeit(stmt="(\"Chicago Bulls\", \"La Lakers\", \"Memphis Grizzlies\", \"Golden State Warriors\", \"Miami Heat\", \"New Orleans Pelicans\")"
						,number=100000000), "seconds")