# Find the smallest of three numbers

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

# Compare The Numbers
if a <= b and a <= c:
    print("Smallest Number is:", a)
elif b <= a and b <= c:
    print("Smallest Number is:", b)
else:
    print("Smallest Number is:", c)