
text = input("Enter a string: ")
count = 0
# Count each vowel, ignoring uppercase/lowercase
for ch in text.lower():
    if ch in "aeiou":
        count = count + 1
# Display the vowel count
print("Number of vowels =", count)