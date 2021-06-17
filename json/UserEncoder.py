from json import JSONEncoder
from User import User
class UserEncoder(JSONEncoder):
	def default(self, o):
		if isinstance(o, User):
			return {"name": o._name, "age": o._age, o.__class__.__name__:True}
		return JSONEncoder.default(self, o)
