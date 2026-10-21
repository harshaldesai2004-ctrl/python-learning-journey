# Print the first n multiples of a number
num = int(input("Enter a number: "))
n = int(input("Enter how many multiples: "))
i = 1
while i <= n:
    print(num * i)
    i += 1