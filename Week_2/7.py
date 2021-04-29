#Swaping Variables
print("Swaping with temperory variable")
x = input("x= ")
y = input("y= ")
temp = "a"
temp = x
x = y
y = temp
print(f"x = {x}")
print(f"y = {y}")

print("Swaping without temperory variable")
x = input("x= ")
y = input("y= ")
x,y = y,x
print("x = ", x)
print("y = ", y)