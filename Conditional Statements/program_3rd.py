
# Program to check voter eligible for voting
age = int(input("Enter your Age: "))

# Check whether the person is 18 or older
if age >= 18:
    # If age is 18 or above, the person is eligible to vote
    print("You Are Eligible To Vote.")
else:
    # If age is below 18, the person is not eligible to vote
    print("You Are Not Eligible To Vote.")
