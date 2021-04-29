#To calculate the full minute and a full hour passed since midnight
#N is the number of seconds
N = int(input("Seconds passed since midnight: "))
#H is the number of hours and M is the number of minutes
H = N//3600
M = N//60
print(f"{H} full hour and {M} full minute passed since midnight")