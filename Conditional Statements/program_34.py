# Check leap year and century year

year = int(input("Enter a year: "))

# Check whether the year is valid
if year <= 0:
    print("Invalid year")
else:
    # Check century year
    if year % 100 == 0:
        print("Century year")
    else:
        print("Not a century year")

    # Check leap year
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Leap year")
    else:
        print("Not a leap year")