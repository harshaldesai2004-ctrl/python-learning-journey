# Check whether a number is a Strong Number
num = int(input("Enter a number: "))
original = num
total = 0
while num > 0:
    digit = num % 10
    fact = 1
    i = 1
    # Calculate factorial of the digit
    while i <= digit:
        fact *= i
        i += 1
    total += fact
    num = num // 10
# Compare the sum with the original number
if total == original:
    print("Strong Number")
else:
    print("Not a Strong Number")