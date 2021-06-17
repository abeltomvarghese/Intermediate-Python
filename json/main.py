import json
from User import User
from UserEncoder import UserEncoder

def JSONencoder(obj):
	if isinstance(obj, User):
		return {"name": obj._name, "age": obj._age, obj.__class__.__name__:True}
	else:
		raise TypeError("This object is not of type user")

def JSONdecoder(dct):
	if User.__name__ in dct:
		return User(name=dct['name'], age=dct['age'])

if __name__ == '__main__':
	person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

	#CONVERT TO JSON
	personJSON = json.dumps(person, indent=4)
	print(personJSON)

	#WRITING TO JSON FILE
	with open("person.json","w") as file:
		json.dump(person, file, indent=4)

	#CONVERTING FROM JSON TO DICTIONARY
	personDict = json.loads(personJSON)
	print(personDict)

	#READING FROM A JSON FILE
	with open("example.json", "r") as file:
		tenant = json.load(file)

	print(tenant)

	superman = User("Clark Kent", 30)

	heroJson = json.dumps(superman, default=JSONencoder, indent=4)
	print(heroJson)

	batman = User("Bruce Wayne", 35)
	dkJson = UserEncoder().encode(batman)
	print(dkJson)

	darkKnight = json.loads(dkJson, object_hook=JSONdecoder)
	print(type(darkKnight))
	print(darkKnight._name)
	print(darkKnight._age)

