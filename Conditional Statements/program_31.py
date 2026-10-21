# Check positive and even number using nested if

num = int(input("Enter a number: "))

# Check whether number is positive
if num > 0:
    # Check whether number is even
    if num % 2 == 0:
        print("Positive and even number")
    else:
        print("Positive but odd number")
else:
    print("Number is not positive")