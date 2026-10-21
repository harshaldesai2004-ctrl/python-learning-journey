# Calculate the Sum of Cubes of First n numbers
num= int(input("Enter num: "))
total = 0
i = 1
while i <= num:
    total += i * i * i
    i += 1
print("Sum of cubes =", total)