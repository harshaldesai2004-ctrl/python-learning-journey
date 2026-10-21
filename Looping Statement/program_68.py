#Check each number from 2 to 50
for num in range(2, 51):
    is_prime = True
    # Check whether num has a divisor
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    # Print only prime numbers
    if is_prime:
        print(num)