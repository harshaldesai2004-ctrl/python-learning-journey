
text = input("Enter a String: ")
reverse = ""
# Add each character to the beginning
for ch in text:
    reverse = ch + reverse
# Display the reversed string
print("Reversed String =", reverse)