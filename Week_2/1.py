#The year when the user turns 100 year old 
name = input("Enter your name:\n").title()
age = int(input("Enter your age:\n"))
year = 2020 + 100 - age
if age < 100 :
    print(f"{name} will turn 100 year old in the year {year}")
else :
    print("You are already 100 year old")