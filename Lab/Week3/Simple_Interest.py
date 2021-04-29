#To calculate the simple interest
#Get the input of Principal amount, rate and period of time
deposit_amount = int(input("Amount of money deposited in the account: "))
rate = float(input("Rate of interest per year(in percentage): "))
year = int(input("Number of years passed after the the deposit: "))
#Calculate interest using the formula
Interest = deposit_amount * (rate/100)*year
#Print the interest amount
print(f"The interest received after {year} years is Rs.{Interest}" )
