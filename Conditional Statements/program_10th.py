# Check whether a number is single-digit or not

num = int(input("Enter a Number: "))

# Check if the number is between -9 and 9
if -9 <= num <= 9:
    print("Single-Digit Number")
else:
    print("Not a Single-Digit Number")