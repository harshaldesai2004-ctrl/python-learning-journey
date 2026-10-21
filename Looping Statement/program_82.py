
base = float(input("Enter the Base: "))
exponent = int(input("Enter a non-negative Integer Exponent: "))
# Multiply the base repeatedly
result = 1
for i in range(exponent):
    result = result * base
# Display the result
print("Answer =", result)