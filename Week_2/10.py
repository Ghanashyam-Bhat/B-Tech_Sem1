#Sum of the digits of given number
give_number = input("Enter a number: ")
sum = 0
for i in give_number:
    sum += int(i)
    print(i)
print(f"Sum : {sum}")