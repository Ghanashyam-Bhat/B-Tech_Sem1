#TO convet distance in Km to m , cm , feet and inches
distance_in_km = int(input("Enter the distance in Km : "))
distance_in_m = distance_in_km * 10**(3)
distance_in_cm = distance_in_m * 10**(2)
distance_in_feet = distance_in_m * 3.281
distance_in_inches = distance_in_feet * 12
print(str(distance_in_m) + " m")
print(str(distance_in_cm) + " cm")
print(str(distance_in_feet)+ " feet")
print(str(distance_in_inches)+ "inch")