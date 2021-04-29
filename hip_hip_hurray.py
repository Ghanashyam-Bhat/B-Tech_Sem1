def rec(a):
	if a!=0 :
		return "hip"+" "+rec(a-1)
	elif a == 0:
		return "hurray"

print(rec(3))