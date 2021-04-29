a = ord("a")
z = ord("z")
A = ord("A")
Z = ord("Z")
lower_case = []
upper_case = []
digits = list(range(10))
spcl = ['$' , '#' , '@']
while a<=z :
	lower_case.append(chr(a))
	a+= 1
while A <= Z :
	upper_case.append(chr(A))
	A += 1
#print(digits)
#print(spcl)
#print(lower_case)
#print(upper_case)
password = input("> ")
password = list(password)
a = 0
A = 0
d = 0
s = 0
#print(password)
for i in password:
	if i in lower_case:
		a += 1
	elif i in upper_case:
		A += 1
	elif i in spcl:
		s += 1 
	elif int(i) in digits:
		d += 1
#print(a , A, d, s , len(password))
if a == 0 or A == 0 or d == 0 or s == 0 or len(password) < 6  or len(password) > 12 :
	print('Invalid')
else:
	print('Valid')