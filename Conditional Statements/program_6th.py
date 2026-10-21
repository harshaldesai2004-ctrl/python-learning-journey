#Compare two numbers and print the greater one
# Take two numbers as input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Compare and print the greater one
if a > b:
    print("Greater number is:", a)
elif b > a:
    print("Greater number is:", b)
else:
    print("Both numbers are equal")