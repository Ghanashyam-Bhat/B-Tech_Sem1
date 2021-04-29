l = ["swimming" , "run" , "climbing" , "eat" , "kk"]
x = list()
for i in l:
	if len(i)< 3 :
		x.append(i)
	elif i.endswith("ing"):
		x.append(i[:-3]+"ly")
	else :
		x.append(i+"ing")
print(x)