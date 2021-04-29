#A) fibonacci series till n terms
n = int(input("give n value: "))
l = [0,1]
x = 0
if n>2:
    while x != (n-1):
        l.append(l[-1]+l[-2])
        x+= 1
elif n == 1:
    l.pop()
elif n ==2 :
    pass
else:
    l = []
print(l)

#B) To find factorial of a number
n = int(input("Give the n value to find n!: "))
x = 0
z = 1
while x != n:
    z *= (n-x)
    x += 1
print(z)

# C) Prime number generator
n = int(input("> "))
x = []
for i in range(2,n+1):
	y = 0
	for j in range(2,i//2+1):
		if i%j==0:
			y+=1
	if y==0:
		x.append(i)
print(x)