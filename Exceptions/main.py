# Common Errors: TypeError, SyntaxError, ModuleNotFoundError, NameError, FileNotFoundError, ValueError, KeyError, ZeroDivisionError
class ValueTooHighError(Exception):
	pass

class ValueNegativeError(Exception):
	def __init__(self, message, value):
		self.message = message
		self.value = value

def test_value(x):
	if x > 1000:
		raise ValueTooHighError("Temperature too high for reactor")
	elif x < 0:
		raise ValueNegativeError("ERROR: Temperature is too cold!!!", x)


if __name__ == '__main__':
	print("RAISING ERRORS")
	speed = 5
	if (speed < 0):
		raise Exception("Speed must be a positive value")
	assert (speed >= 0), "Speed must be a positive val"

	print("CATCHING & HANDLING ERRORS")

	try:
		# a = 5 / 0
		# b = a + "b"
		c = 5 + 6
	except ZeroDivisionError as e:
		print("You cannot divide by zero")
	except TypeError as te:
		print("You are better than this - Come on!")
	else:
		print("Process completed Successfully")
	finally:
		print("This clause runs everytime - useful for clean up - file handling etc")

	print("CREATING YOUR OWN ERRORS")
	try:
		#test_value(1001)
		test_value(-49)
	except ValueTooHighError as e:
		print(e)
	except ValueNegativeError as vne:
		print(vne.message, vne.value)