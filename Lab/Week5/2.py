#2.a.
s='Respected sir,\n I am here By enlisting all the programming languages  we teach.\n Problem solving using python.\n object oriented programming with C++\n java and jee. \n R programming. \n Thanking You \n Team Programming Languages'
line = s.split("\n");
for i in line:
    print(i.capitalize())
print()
#2.b
mac=['00','11','23','45','67','70']
address=''
for m in mac:
	address+=m
print('the mac address is',address)
print()
#2.c
l=['a','b','c','d']
for i in l:
	print('dear',i,'happy holi')
print()
#2.d.
given = input("SRN: ")
srn = "PESU20CS153 PESU20CS154 PESU20CS155 PESU20CS156 PESU20CS157 PESU20CS158"
print(srn)
l = list(srn.split())
if given in l:
	print("The given SRN is present")
else:
	print("The given SRN is not present")

r = []
for i in l[:3]:
	z = list(i)
	y = 0
	while y<=3:
		y+=1
		z.pop(0)
	z.insert(0,"P")
	z.insert(1,"E")
	l.remove(i)
	s = ""
	for j in z:
		s+=j
	r.append(s)
r.extend(l)
print(r)
