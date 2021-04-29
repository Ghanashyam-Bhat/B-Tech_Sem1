#Swap the alphabets
#Take the input from the user
n = input("Enter the sequence of character: ").lower()
l = list(n)
#Convert the input into list
new = ""
for x in l :
	z=ord(x)
#Get the asci values, update the values
	if z == 122 :
		new += "a"
	else:
		new += chr(z+1)
#print the output
print(new)