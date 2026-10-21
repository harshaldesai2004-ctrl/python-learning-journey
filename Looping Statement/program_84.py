
text = input("Enter a String: ")
# Reverse the string
reverse = text[::-1]
# Compare without considering letter case
if text.lower() == reverse.lower():
    print("Palindrome string")
else:
    print("Not a palindrome string")