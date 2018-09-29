mytuple = ("apple","banana","cherry")
myit = iter(mytuple)

print(myit)
print(next(myit))
print(next(myit))
print(next(myit))

	
print('\nstring example\n')

print(mytuple[1])
myit_b = iter(mytuple[1])
print(next(myit_b))
print(next(myit_b))
print(next(myit_b))

for x in myit_b:
	print(x)
	
print('\n__iter__ and __next__ examples\n')

class MyNumbers:
	def __init__(self):
		self.a = 3		
	def __iter__(self):
		self.a = 1
		return self
	def __next__(self):
		if self.a<20:
			x = self.a
			self.a += 1
			return x
		else:
			raise StopIteration

myclass = MyNumbers()
print("Class : " + str(myclass.a))

myiter = iter(myclass)

print("Class : " + str(myclass.a))
print(next(myiter))
print("Class : " + str(myclass.a))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print("Class : " + str(myclass.a))

print('\nraise StopIteration example\n')

for x in myiter:
	print(x)