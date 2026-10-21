# Take a Non-Negative Integer From the User
num = int(input("Enter a Non-Negative Number: "))
digits = str(num)
power = len(digits)
total = 0
# Add each digit raised to the number of Digits
for ch in digits:
    total = total + int(ch) ** power
# Compare the total with the original number
if total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")