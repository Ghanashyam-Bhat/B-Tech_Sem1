file = open("z.txt","r")
rd = file.readlines()
file.close()
print(len(rd))


l = []
for i in rd:
	l.extend(i.split(" "))
print(len(l))

l1 = l.copy()
for i in l:
	if i.endswith("\n"):
		l1.remove(i)
		l1.append(i[:-1])
x = []
for  i in l1:
	x.extend(list(i))
print(len(x))
