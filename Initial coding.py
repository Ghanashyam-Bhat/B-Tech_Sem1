#1st lesson
name=input('Wt is ur name?')
print('hello'+' '+name)
colour=input('What is your favorite colour? ' )
print('Wow,'+' '+name+' likes'+' '+colour)
birth_year=input('Birth Year: ')
age=2020-int(birth_year)
print(age)
weight_in_kilograms=input('What is your weight? ')
weight_in_grams=(10**3)*float(weight_in_kilograms)
print(weight_in_grams)

#2nd lesson
first_name=input('First Name: ')
last_name=input('Last name: ')
#print(first_name+" "+'['+last_name+'] is a coder')
message=f'{first_name}[{last_name}] is a coder'
print(message)

#3rd lesson
course='python for beginners'
yes_or_no=('python' in course)
print(yes_or_no)
print(course.upper())
print(len(course))

#4th lesson
word1='Hello sir, '
word2='How can I help you?'
answer=input(word1+word2)
print('Ok sir. I will be back in a minute')
print('''The task''','"'+answer+'"','is compleated sir.')

#5th lesson
import math
print(math.log2(4))
print(5+3*2**2-4)
print((5+3)*2**2-2)

#6th lesson
is_hot=False
is_cold=False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

#My project 1
question=input('Is it a hot day?(Y/N) ')
info='Yes'
is_hot=question in info
if is_hot:
    print("Drink plenty of water")
    print("Protect yourself from harsh sun rays")
else:
    print('Enjoy your day!!')

#My project 2
full_name=input('What is your name? ')
print('Hello'+' '+full_name.upper())
print('Welcome to our page!!')
colours_selection='RED GREEN BLUE YELLOW BLACK BROWN ORANGE VIOLET GREY WHITE GOLD SILVER'
print('Select one among these colours: Red, Green, Blue, Yellow, Black, Brown, Orange, Violet, Grey, White, Gold, Silver')
colour=input('What is your favorite colour? ')
colour_selected=colour.upper() in colours_selection
if colour_selected:
    print('Ohh!'+' '+full_name.upper()+"'s favorite colour is"+' '+colour.upper())
else:
    print('There is an error in the word you have enterd. Please check the spelling you have enterd.')


#7th Lesson
name_enterd=input('Enter your name: ')
less_than_reqd=len(name_enterd)<4
more_than_reqd=len(name_enterd)>50
if less_than_reqd:
    print('The name you have entered must have more than 3 charecters.')
elif more_than_reqd:
    print("The name you have entered must have less than 50 charecter.")
else:
    print('The name looks good!')


#8th lesson
weight_entered=input("What is our weight?" )
unit_is_kg='K'
unit_is_pound='L'
print("Type 'L' if it is in pound or type 'K' if it is in Kg.")
entered_unit =input("What is the the unit of the weight entered? ")
convert_from_kg = entered_unit.upper() in unit_is_kg
convert_from_pound=entered_unit.upper() in unit_is_pound
if convert_from_kg:
    print(str(float(weight_entered)/0.45)+' lbs')
elif convert_from_pound:
    print(str(float(weight_entered)*0.45)+' Kg')
else:
    print('There is something error in the charecters you have enetred')

#9th lesson
print("Enter 'help' for controls")
while True:
    command=input('> ').lower()
    if command=='start':
        print('The car has been started.')
    elif command=='stop':
        print('The car has been stopped.')
    elif command=='help':
        print("""
        Enter
        start- Start the car
        stop - To stop the car
        quit- To quit the game
        """)
    elif command=='quit':
        break
    else:
        print("I dont understand!!")
print('The game has been ended.')

#My project 3
#Registration for Marathon 2020
print("Welcome to registration of Marathon 2020. PLease note that age limit is 20-40. Please provide the necessary details to compleate the varification for eligibility.")
print("Notice: Participants whose details are found fake will be disqualified from the compitition")
print("The name must conatin atleast 3 charecters and atmost 20 charecters.")
print("Provide the active email ID so that we can conatct you to deliver information about the Marathon-2020")
name = input("Name: ").upper()
birth_year = int(input("Birth Year: "))
age = 2020-birth_year
email = input("Enter your email ID: ").lower()
if email[-10:] != '@gmail.com':
    print("Invalid email ID! Please enter a valid email ID.")
elif len(name)<3:
    print("Your name is too short to register!")
elif len(name)>20:
    print("Your name is too long!")
elif age<20:
    print("Oops! You are too young to participate in the compitition.")
    age_diff = 20-age
    print(f"Wait {age_diff} years to participate.")
elif age > 40:
    print("Sorry you cannot take part in the compition, because you have crossed the age limit.")
else:
    print(f"""
Welcome {name} to the Marathon-2020
You are fully eligible to prticipate in compitition.
We will send the date, venue and other related information of the compitition to your email ID {email}.
Thank you.""")

#My project 4
#A proper car game
info="""
start- To start the car
stop- To stop the car
end - To quit the game"""
print("Enter 'info' for controls")
while True:
    command=input("> ").lower()
    if command=='stop':
        print("The car is already at rest. Please start the car.")
    elif command=='info':
        print(info)
    elif command=='start':
        print("The car has been started.")
        while True:
            given=input("> ")
            if given=="start":
                print("The car is already started.")
            elif given=="stop":
                print("The car has been stopped")
                break
            elif given=="info":
                print(info)
            elif given=="end":
                print("The car has to be stopped first to end the game.")
            else:
                print("I don't understand")
    elif command=="end":
        print("The game has been ended")
        break
    else:
        print("I don't understand!")

#Project 5
no_of_bottles = int(input("Total number of bottles on the wall: "))
while no_of_bottles > 0 :
    print(f"There are {no_of_bottles} bottles on the wall")
    no_of_bottles -= 1
print("No more bottles on the wall")

