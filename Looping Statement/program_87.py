# Print numbers until a negative number is entered

while True:
    num = int(input("Enter a number: "))

    if num < 0:
        break

    print(num)