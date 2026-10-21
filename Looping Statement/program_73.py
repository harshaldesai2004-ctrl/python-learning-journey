
num = abs(int(input("Enter a Number: ")))
total = 0
# Check each digit and add odd Digits
while num > 0:
    digit = num % 10
    if digit % 2 != 0:
        total = total + digit
    num = num // 10
# Display the sum of odd Digits
print("Sum of odd digits =", total)