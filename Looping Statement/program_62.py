# Take a number from the user
num = int(input("Enter a Number: "))
# Store the sign and work with the absolute value
sign = -1 if num < 0 else 1
num = abs(num)
reverse = 0
# Reverse the Digits One by One
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
# Display The Reversed Number
print("Reversed Number =", sign * reverse)