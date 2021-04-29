string = "jfvsdhukbvjbfvjdjvbjhfvdkdjhhjfbkjdfb jldlbkdfkjbdkbjdnbkfbkjdnbnj"
l = list(string) 
first = l[0]
for i in range(l.count(first)):
	l.insert(l.index(first) , "$")
	l.remove(first)
l.pop(0)
l.insert(0,first)


che = ""
for i in l:
	che+= i
print(che)