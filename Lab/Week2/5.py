#To convert degree celcius to Farenheit and vice-versa
temp = float(input("What is the temperature:\n"))
unit = input("Enter 'C' for celcius and 'F' for farenhiet: ").upper()
if unit == "C" :
    ans = str((9/5)*(temp)+32)+ " F"
elif unit == "F" :
    ans = str((temp - 32)*(5/9)) + " C"
print(ans)