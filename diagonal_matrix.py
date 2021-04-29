print([[5,0,0,0] , [0,5,0,0], [0,0,5,0], [0,0,0,5]])
n = 0
x = 5
l = []
while n<4:
	z = []
	for i in range(4):
		if i==n:
			z.append(x)
		else :
			z.append(0)
	l.append(z)
	n+=1
print(l)