
num = int(input("Enter a Number: "))
is_prime = num >= 2
# Check possible divisors
for i in range(2, int(max(num, 0) ** 0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
# Display the result
if is_prime:
    print("Prime Number")
else:
    print("Not a Prime Number")