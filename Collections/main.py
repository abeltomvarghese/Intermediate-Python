from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque
if __name__ == '__main__':
	#Collections: Counter

	a = "aaaabbbcc"
	my_counter = Counter(a)
	print(my_counter)
	print(my_counter.items())
	print(my_counter.values())
	print(my_counter.most_common(2)[0][0])
	print(list(my_counter.elements()))


	#Collections: NamedTuple
	Name = namedtuple("Name", 'firstName,surname,sport')

	michaelJordan = Name("Michael", "Jordan", "Basketball")
	tomBrady = Name("Tom", "Brady", "American Football")
	cristianoRonaldo = Name("Cristiano", "Ronaldo", "Football")

	goatList = []
	goatList.append(michaelJordan)
	goatList.append(tomBrady)
	goatList.append(cristianoRonaldo)

	for fName,sName,sport in goatList:
		print(f"Name: {fName} {sName} Sport: {sport}")


	#Collections: Ordered Dictionary

	legendsDict = OrderedDict()

	legendsDict["NFL"] = tomBrady
	legendsDict["EPL"] = cristianoRonaldo
	legendsDict["NBA"] = michaelJordan

	print(legendsDict)

	#Collections: default dictionary
	garage = defaultdict(str)

	garage['luxury'] = "S-Class"
	garage['family'] = "Range Rover"
	garage['supercar'] = 'Aventador'
	garage['legacy'] = 'SLR Mclaren'
	garage['ultra-luxury'] = 'Phantom'

	print(garage)
	print(garage['ultra-luxury'])

	#Collections: Deque
	nums = deque()

	nums.append(2)
	nums.append(3)

	nums.appendleft(1)

	nums.extend([4,5,6])
	nums.extendleft([0,-1,-2,-3,-4,-5])

	print(nums)

	nums.pop();
	print(nums)

	nums.popleft()
	print(nums)

	# shifting all elements to the right

	nums.rotate(1)  #shifts the numbers in nums by 1 to the right
	print(nums)

	nums.rotate(-1) #shifts the numbers in nums by 1 to the left
	print(nums)