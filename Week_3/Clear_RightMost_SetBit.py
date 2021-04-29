
#To clear right most set bit
n = int(input("Enter an number: "))
#Convert the entered value into binary
print(f"Binary value of the entered number {bin(n)}")
if n%2 == 0 :
	print("The last bit of a even number is always a set")
else :
#Clearing the last set bit and printing the binary value
	print("After clearing last set bit")
	z = n&(n-1)
	print(bin(z))
