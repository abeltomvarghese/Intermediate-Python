
def greet(yourName, myName):
	print(f'Hi {yourName}, my name is {myName}')

def saved(rescued = 100):
	print(f'I\'ve rescued {rescued} people')

def puzzleUp(a, b, *args, **kwargs):
	print(a, b)

	for arg in args:
		print(arg)

	for key in kwargs:
		print(key, kwargs[key])

def printNums(*args, last):
	for arg in args:
		print(arg)

	print(last)

def printList(a, b, c):
	print(a,b,c)


if __name__ == '__main__':

	batman = 'Bruce Wayne'
	capAmerica = 'Steve Rogers'

	greet(batman, capAmerica) #positional arguments
	greet(myName=capAmerica, yourName=batman) #keyword arguments

	#method has default values
	saved(252)

	print('\n')

	myDict = {}
	myDict['superPower'] = "Flying"
	myDict['Agency'] = "Kal-El"

	puzzleUp(1,2,3,4,5, superPower='flying', agency='Kal-el')
	puzzleUp(1,2,(3,4,5), myDict)

	printNums(1,2,3,4,5,6,7, last=10)

	#UNPACKING A ITERABLE TO BE USED IN A FUNCTION
	numsList = [1,2,3]
	numTuple = (1,2,3)
	numDict = {'a':1, 'b':2, 'c':3}

	printList(*numsList)
	printList(*numTuple)
	printList(**numDict)

