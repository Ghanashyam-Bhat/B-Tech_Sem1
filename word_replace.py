string = "how much wood would a wood chuck chuck if a wood chuck could chuck wood"
l = string.split(" ")
d = dict()
l1 = list()
l2 = list()
for i in l:
	if i[0] not in l1:
		l1.append(i[0])
for i in l1:
	s = set()
	for j in l:
		if j.startswith(i):
			s.add(j)
	l2.append(s)

x = dict(zip(l1,l2))
print(x)