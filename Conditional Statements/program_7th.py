# Program to check whether a character is a vowel or consonant
ch = input("Enter a Character: ")

# Check Whether The Character Is a Vowel
if ch.lower() in 'aeiou' and len(ch) == 1:
    print("The character is a vowel.")

# Check whether the character is a consonant
elif ch.isalpha() and len(ch) == 1:
    print("The Character is a Consonant.")

else:
    print("Please Enter a Single Alphabet.")