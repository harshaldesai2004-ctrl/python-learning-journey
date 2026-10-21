# Check divisibility by both 3 and 7

num = int(input("Enter a number: "))

# Check divisibility
if num % 3 == 0 and num % 7 == 0:
    print("Number is divisible by both 3 and 7")
else:
    print("Number is not divisible by both 3 and 7")