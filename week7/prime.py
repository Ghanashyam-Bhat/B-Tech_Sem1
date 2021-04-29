def fun(a):
	r = list(range(2,a+1))
	l = []
	r = []
	s = []
	x = 2
	def f():
		i = r[0]
		while i*x<=a:
			s.append(i*x)
			x+=1
	f()
fun(5)