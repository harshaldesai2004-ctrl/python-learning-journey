# Take a number from the user
num = int(input("Enter a number: "))
# Store the original number
original = num
temp = abs(num)
reverse = 0
# Reverse The Digits
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10
# Compare original and Reversed Numbers
if num >= 0 and original == reverse:
    print("Palindrome number")
else:
    print("Not a Palindrome number")