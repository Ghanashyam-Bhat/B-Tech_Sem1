l = [65,115,120,50,136,94,87,100]
x = 0
y = 0
for i in l :
	if 50<=i and i<=65:
		print("bradycardia")
		x+=1
	elif i>=100:
		print("tachycardia")
		y+= 1 
	else :
		print("Normal")
if x > 3:
	print("risk, bradycardia exceeded 3 count")
if y > 3 :
	print("risk, tachycardia exceeded 3 count")
print("maximim heart beat rate",max(l))
print("minimum heart beat rate",min(l))
