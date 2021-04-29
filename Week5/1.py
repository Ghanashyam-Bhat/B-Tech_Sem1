
l=['panipuri','dosa','bhelpuri','masaladosa','dahipuri','ravadosa','pizzamania','pizza topping']
l1=[];l2=[];l3=[]
for i in l:
	if i.startswith('pizza'):
		l1.append(i)
	elif i.endswith('puri'):
		l2.append(i)
	elif i.endswith('dosa'):
		l3.append(i)
print(l1)
print(l2)
print(l3)