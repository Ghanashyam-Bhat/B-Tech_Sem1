l = [65,98,96,94,98,32,65,84,75,68,98,94,93,92,94,97,91,85,65,14,74,53,42]
print("maximum marks scored is",max(l))
print("number of students who scored maximum marks is",l.count(max(l)))
fail = 35
x = 0
z = max(l)
for i in l:
	if i==max(l):
		l.remove(i)
		x+=1
print("second highest is",max(l))
while x!=0:
	l.append(z)
	x -=1
for i in l:
	if i< fail:
		l.remove(i)
print(l)