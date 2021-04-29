#A) To get single charecter from a string
print("A)")
given_string = "CsPythonLab"
import random
print(random.choice(given_string))
print("""
""")

#Dont assign any any random function to a new variable
#dont do x = random.choice(p)

#B) Choosing CR for class of 10 students
print("B)")
import random as r
class_room = [1,2,3,4,5,6,7,8,9,10]
r.shuffle(class_room)
print(class_room)
print(r.choice(class_room))
print(r.sample(class_room,2))
print(r.sample(class_room,4))
print("""
""")

#C) To multiply 2 random floating numbers
print("C)")
import random
a = random.random()
b = random.random()
print("a= ",a)
print("b= ",b)
c = a*b
print("c= ",c)
print("""
""")

#D) Generate a random floating point number
print("D)")
import random
print(random.uniform(8.0,10.0))
print("""
""")

#E) Generate some random integer from given range
print("E)")
import random
print(random.randrange(10,15))
print("""
""")

#F) Program to generate same random number every time
print("F)")
import random
random.seed(2230)
print(random.randint(5,10))
print("""
""")

#G) Roll a dice so that you always get same number
print("G)")
import random as r
r.seed(10)
print(r.randint(1,6))

