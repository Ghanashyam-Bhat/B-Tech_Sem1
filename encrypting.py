stri = input("> ")
l = list(stri)
n = int(input("Give a encryption value: "))
l1 = list()
final = ""
for i in l:
	l1.append(chr(ord(i)+n))
for j in l1:
	final += j
print(final)