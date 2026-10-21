
text = input("Enter a string: ")
count = 0
# Count Alphabetic Characters That Are Not Vowels
for ch in text.lower():
    if ch.isalpha() and ch not in "aeiou":
        count = count + 1
# Display the consonant count
print("Number of consonants =", count)
