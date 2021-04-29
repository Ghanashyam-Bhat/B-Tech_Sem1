#4 Jan 2021
#To determine the day of the week
year = int(input("> "))
year_count = 1
no_of_days_in_previous_year = 0
while year_count != year:
    if year_count % 100 == 0:
        if year_count % 400 == 0:
            no_of_days_in_previous_year += 366
        else :
            no_of_days_in_previous_year += 365
    elif year_count % 4 == 0:
        no_of_days_in_previous_year += 366
    else :
        no_of_days_in_previous_year += 365
    year_count += 1
no_of_days_in_previous_year += 24
if no_of_days_in_previous_year % 7 == 0:
    print("Sunday")
if no_of_days_in_previous_year % 7 == 5 :
    print("Friday")
print(no_of_days_in_previous_year % 7)
print(no_of_days_in_previous_year)

