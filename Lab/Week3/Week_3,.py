#To convert "abc" into "bcd"
"""print("enter a charecter")
char = input("Enter a digit ").lower()
to_be_list = ""
for i in char :
    to_be_list += i
    to_be_list += " "
list = to_be_list.split(" ")
for x in list :
    z = ord(char)
    if z == 122 :
        print("a")
    else :
        print(chr(z+1))"""

#Program to swap contents of 2 memory locations using bit-wise operators
#No temporary variable or arithmatic operators
"""a = input("Enter the value of a ")
b = input("Enter teh value og b ")
a,b = b,a
print(a,"\n"+b)"""
"""a = int(input("Enter the value of a "))
b = int(input("Enter teh value og b "))
a = a^b
b = a^b
a = a^b
print(a)
print(b)"""

#To clear right most set bit
"""n = int(input("Enter Number: "))
print(bin(n))
print("After clearing last set")
z = n&(n-1)
print(bin(z))"""

#To multiply 2 random floating numbers
"""import random
a = random.random()
b = random.random()
print("a= ",a)
print("b= ",b)
c = a*b
print("c= ",c)"""

#To multiply 2 random floating numbers range from 10.5 to 20.5
"""import random
a = random.uniform(10.5,20.5)
b = random.uniform(10.5,20.5)
print("a= ",a)
print("b= ",b)
c = a*b
print("c= ",c)"""

#Program to generate same random number every time
"""import random
random.seed(2230)
print(random.randint(5,10))"""

#Roll a dice so that you always get same number
"""import random as r
r.seed(10)
print(r.randint(1,6))"""

#
"""import random as r
class_room = [1,2,3,4,5,6,7,8,9,10]
r.shuffle(class_room)
print(class_room)
print(r.choice(class_room))
print(r.sample(class_room,2))
print(r.sample(class_room,4))"""

#To shuffle random charecter from the string
"""import random
p = "python"
print(random.choice(p))"""
#Dont assign any any random function to a new variable
#dont do x = random.choice(p)