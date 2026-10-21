
num = abs(int(input("Enter a Number: ")))
# Convert To String and Find the Largest Digit
largest = 0
for ch in str(num):
    digit = int(ch)
    if digit > largest:
        largest = digit
# Display The Largest Digit
print("Largest digit =", largest)