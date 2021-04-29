#Distance between two points A and B
print("Enter the values of cordinates A(X1 , y1) and B(x2 , y2) ")
x1 = int(input  ("x1: "))
y1 = int(input  ("y1: "))
x2 = int(input  ("x2: "))
y2 = int(input  ("y2: "))
z  = ((x1 - x2)**2 + (y1 - y2)** 2)**0.5
print("The distance between two poins A and B is", z)