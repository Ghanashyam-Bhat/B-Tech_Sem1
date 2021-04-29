def fibonacci(x):
	l = []
	def f(a):
		if a==1:
			return 1
		if a==2:
			return 1
		if a>2:
			return f(a-1)+f(a-2)
	for i in range(1,x+1):
		l.append(f(i))
	return l
print(fibonacci(5))