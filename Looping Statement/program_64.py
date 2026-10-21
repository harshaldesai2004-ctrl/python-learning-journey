
n = int(input("Enter number : "))
# Start with the first two Fibonacci numbers
a, b = 0, 1
# Print n terms
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
