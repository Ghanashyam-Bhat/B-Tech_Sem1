file = open("z.txt", "r")
rd = list(file.read())
file.close()
u = 0
l = 0
for i in rd:
	if i.islower():
		l+=1
	elif i.isupper():
		u+=1
writing = open("k.txt","w")
print("Uppercase" , u,"\n","Lowercase",l,file=writing)
writing.close()