#Gravitational force between two objects
#Take the input of masses and the distance between them
m1 = float(input("Mass of 1st object(in kg): "))
m2 = float(input("Mass of 2nd object(in kg): "))
r = float(input("Distance between two masses(in m): "))
G = 6.67 * 10**(-11)
#Formula to find the gravitational force
F = (G * (m1 * m2) / (r**2))
#print the result
print(F)