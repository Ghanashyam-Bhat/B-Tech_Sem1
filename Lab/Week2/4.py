#To find the time difference between two time stamps seconds
hr1 = int (input("hr1 : "))
min1 = int (input("min1: "))
sec1 = int (input("sec1: "))
hr2 = int (input("hr2: "))
min2 = int (input("min2: "))
sec2 = int (input("sec2: "))
hr1*= 3600
min1*= 60
ttl1 = hr1 + min1 + sec1
hr2 *= 3600
min2 *= 60
ttl2 = hr2 + min2 + sec2
difference = abs(ttl2 - ttl1)
print(f"Time difference {difference} seconds")