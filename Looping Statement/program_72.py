
num = abs(int(input("Enter a Number: ")))
total = 0
# Check each digit and add Even Digits
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        total = total + digit
    num = num // 10
# Display the sum of Even Digits
print("Sum of even digits =", total)