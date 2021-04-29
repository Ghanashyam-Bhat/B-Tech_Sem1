def my_power(a,b):
	if b==1:
		return a
	else :
		b -= 1
		return a*my_power(a,b)

print(my_power(3,2))