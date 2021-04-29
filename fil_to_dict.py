"""python computational problem
python modules
python files
user defined python modules
problem solving using python"""

file = open("z.txt","r")
rd = file.readlines()
file.close()


l = []
for i in rd:
	l.extend(i.split(" "))


l1 = l.copy()
for i in l:
	if i.endswith("\n"):
		l1.remove(i)
		l1.append(i[:-1])


dict = {}
for i in l1:
	x = l1.count(i)
	dict[i] = x

print(dict)


"""Output:
{'python': 5, 'computational': 1, 'user': 1, 'defined': 1, 'problem': 2, 'solving': 1, 'using': 1, 'modules': 2, 'files': 1}"""