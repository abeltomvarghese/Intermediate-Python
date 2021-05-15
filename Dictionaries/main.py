if __name__ == '__main__':
	carDict = {"name":"Mercedes","model": "S-Class", "year":2021, "wheelbase":"ewb"}
	print(carDict)

	goat = dict(name="Michael Jordan", number=23, team="Chicago Bulls")
	print(goat)

	value = carDict["name"]
	print(value)

	goat["nickname"] = ["Air Jordan", "His Airness"]
	print(goat)

	goat["otherSports"] = "Baseball"
	print(goat)

	#goat.pop("nickname")
	#goat.popItem() removes the last item in the dictionary
	del goat["otherSports"]
	print(goat)

	if "nickname" in goat:
		print(goat["nickname"])


	try:
		print(carDict["modelNum"])
	except:
		print("Error in finding information")

	for key in carDict.keys():
		print(key)

	for value in carDict.values():
		print(value)

	for key, value in goat.items():
		print(key + ":", value)

	goat_copy = goat # now both the copy & original dict points to the same memory location
	goat_cpy = goat.copy() # safe way to copy the dictionary

	# updating two dictionaries
	mercedes = {"variant": "Amg-Line"}
	carDict.update(mercedes)
	print(carDict)

	rookie = ("Zion", "Williamson")
	rookieDict = {rookie: "New Orleans Pelicans"}
	print(rookieDict)