# Take a Positive Number From The User
num = int(input("Enter a positive number: "))
# A factor divides the number without a remainder
for i in range(1, num + 1):
    if num % i == 0:
        print(i)