# Take a Number From The User
num = int(input("Enter a number: "))

# Initialize Factorial
fact = 1

# Calculate Factorial
for i in range(1, num + 1):
    fact = fact * i

# Display The Result
print("Factorial =", fact)