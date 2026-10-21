# Check number of digits

num = int(input("Enter a number: "))
num = abs(num)

# Check number of digits
if num <= 9:
    print("Single-digit number")
elif num <= 99:
    print("Double-digit number")
elif num <= 999:
    print("Three-digit number")
else:
    print("More than three digits")