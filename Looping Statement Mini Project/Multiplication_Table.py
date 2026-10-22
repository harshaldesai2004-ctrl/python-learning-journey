
# Multiplication Table and Number Analyzer
number = int(input("Enter a number: "))
# Print the multiplication table
print("\nMultiplication Table of", number)
for i in range(1, 11):
    print(number, "x", i, "=", number * i)
# Enter the number range
start = int(input("\nEnter starting number: "))
end = int(input("Enter ending number: "))
# Check whether the range is valid
while start > end:
    print("Starting number cannot be greater than ending number.")
    start = int(input("Enter starting number again: "))
    end = int(input("Enter ending number again: "))
even_count = 0
odd_count = 0
total = 0
# Analyze the numbers in the range
for num in range(start, end + 1):
    total = total + num
    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
# Display the result
print("\n--- Number Analysis ---")
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Sum of numbers:", total)
