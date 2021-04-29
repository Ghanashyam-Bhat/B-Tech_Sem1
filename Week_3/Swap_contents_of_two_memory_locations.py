#Program to swap contents of 2 memory locations using bit-wise operators
#No temporary variable or arithmatic operators
a = input("Enter the value of a ")
b = input("Enter teh value og b ")
a,b = b,a
print(a,"\n"+b)
#With XOR
a = int(input("Enter the value of a "))
b = int(input("Enter teh value og b "))
a = a^b
b = a^b
a = a^b
print(a)
print(b)