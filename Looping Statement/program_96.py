# Print numbers from 1 to n, skipping multiples of 3
n = int(input("Enter the limit: "))
i = 1
while i <= n:
    if i % 3 != 0:
        print(i)
    i += 1