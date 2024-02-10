'''Create a program that determines whether a given year is a leap year.
A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination.
'''
# Input = 2024
# output = Leap year

year = int(input("Enter Any Year "))
if year % 4 == 0 and year % 100 != 0:
    print("Its Leap Year")
elif year %400 == 0  and year %100!=0:
    print("Its leap year")
else:
    print("Not a leap year")