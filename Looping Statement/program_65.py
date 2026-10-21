
num = abs(int(input("Enter a Number: ")))
total = 0
# Add each digit to total
while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10
# Display the sum of digits
print("Sum of digits =", total)