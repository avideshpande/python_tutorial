"""def my_function(str = "no val"):
	print("Hello from function")
	print("value passed : "+str)
	return 2*5
my_function()
my_function("avi")

print(my_function())

"""
def myfunc(n):
	return lambda a : a * n
mydoubler  = myfunc(2)
#print(mydoubler)
print(mydoubler(11))
#"""