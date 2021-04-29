def fun(a,b):
	if len(a)>len(b):
		return a
	elif len(a) < len(b):
		return b
	else :
		return a,b

print(fun("hii" , "hello"))