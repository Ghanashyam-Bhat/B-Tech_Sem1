#To find the number of apples lest in the basket after evenly distributed among the students
#Total number of students is N
N = int(input("Total number of students:\n"))
#Total number of apples is K
K = int(input("Total number of apples:\n"))
print(f"Each student gets {K//N} apples")
print(f"{K%N} apples remains in the basket")