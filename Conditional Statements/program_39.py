# Check number range

num = int(input("Enter a number: "))

# Check range excluding 0 and 100
if num > 0 and num < 100:
    print("Number is between 0 and 100")
else:
    print("Number is not between 0 and 100")