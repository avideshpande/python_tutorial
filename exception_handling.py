"""
try:
  print("Hello")
  print(x)
except NameError:
	print("x is not defined")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
	print("finally block")
"""

try:
	#print("Hello")
	print(x)
except NameError:
	print("x is not defined")
except:
	print("Something went wrong")
else:
	print("else block try -- nothing went wrong")
finally:
	print("finally block")
print("outside x")

try:
	y=10
	print(y)
except NameError:
	print("y is not defined")
except:
	print("Something went wrong")
else:
	print("else block try -- nothing went wrong")
finally:
	print("finally block")
print("outside y")
