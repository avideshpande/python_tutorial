def fib(n):
	result = []
	a, b = 0, 1
	while a<n:
		#print(a, end=' ')
		result.append(a)
		a, b = b, a+b
	#print()
	return result
	
f100 = fib(100)
print(f100)