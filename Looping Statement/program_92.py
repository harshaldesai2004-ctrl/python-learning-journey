# Calculate the sum of squares of first n numbers
n = int(input("Enter Number: "))
total = 0
i = 1
while i <= n:
    total += i * i
    i += 1
print("Sum of Squares =", total)