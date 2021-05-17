from timeit import default_timer as timer
if __name__ == '__main__':
	nflLegend = "Tom Brady"

	char = nflLegend[-1]

	print(char)

	crypticMessage = "hbevldlsowWhorrwlhd"
	decrypted = crypticMessage[::2]
	print(decrypted)

	firstName = "Michael"
	lastName = "Jordan"

	fullname = firstName + " " + lastName
	print(fullname)

	for i in fullname:
		print(i)


	if "z" in fullname:
		print("yes")
	else:
		print("No")

	greeting = "       hello        "
	strippedGreeting = greeting.strip()
	print(strippedGreeting)

	print(nflLegend.startswith("T"))
	print(nflLegend.endswith("y"))
	print(nflLegend.find("Brad"))

	print(fullname.count("a"))

	print(fullname.replace("Jordan", "Jackson"))

	shopping = "Banana, orange, apple, mango"
	shoppingList = shopping.split(", ")

	for item in shoppingList:
		print(item)

	new_string = " ".join(shoppingList)
	print(new_string)

	start = timer()
	my_list = ["z"] * 10

	sleep = "".join(my_list)
	print(sleep)
	stop = timer()
	print(stop-start)

	#formatting
	var = 2.34634341
	print("the magic value is %.2f & my name is %s" % (var, fullname))

	#alternative formatting
	print("The magic value is {:.2f} and my name is {}".format(var, fullname))

	#formatting since python 3.6
	print(f"the magic value is {var:.2f} & the greatest player is {fullname}")
