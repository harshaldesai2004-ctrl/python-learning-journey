#Check whether a year is a leap year
# Take a year as input
year = int(input("Enter a year: "))

# Leap year: divisible by 4 
if (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")