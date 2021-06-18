import functools

class CountCalls():
	def __init__(self, func):
		self._func = func
		self._numCalls = 0

	def __call__(self, *args, **kwargs):
		self._numCalls += 1
		print(f'This is executed {self._numCalls} times')
		return self._func(*args,**kwargs)

def repeatDef(num_times):
	def greetingDecorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			for _ in range(num_times):
				result = func(*args, **kwargs)
			return result
		return wrapper
	return greetingDecorator

def add5Decorator(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		print("start")
		result = func(*args, **kwargs)
		print("end")
		return result
	return wrapper

@add5Decorator
def add5(x):
	return x + 5


@repeatDef(num_times=5)
def greeting(name):
	print(f'Greetings {name}')

@CountCalls
def say_hello():
	print('Hello')

if __name__ == '__main__':
	print(add5(15))
	print(add5.__name__)

	greeting("Bruce Wayne")

	say_hello()