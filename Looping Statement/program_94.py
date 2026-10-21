# Print alternate characters of a string
text = input("Enter a string: ")
i = 0
while i < len(text):
    print(text[i], end="")
    i += 2
print()