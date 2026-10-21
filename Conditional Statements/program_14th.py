# Check whether a character is uppercase or lowercase

ch = input("Enter a Character: ")

# Check character
if ch.isupper():
    print("Uppercase Character")
elif ch.islower():
    print("Lowercase Character")
else:
    print("Not an Uppercase or Lowercase Letter")