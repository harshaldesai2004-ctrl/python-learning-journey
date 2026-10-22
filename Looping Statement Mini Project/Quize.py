
# Quiz Application
score = 0

# Ask five questions
print("Welcome to the Python Quiz!")

answer = input("1. What is the capital of India? ").lower()
if answer == "delhi":
    print("Correct answer!")
    score = score + 1
else:
    print("Wrong answer! The correct answer is Delhi.")

answer = input("2. Which language are we learning? ").lower()
if answer == "python":
    print("Correct answer!")
    score = score + 1
else:
    print("Wrong answer! The correct answer is Python.")
answer = input("3. How many days are in a week? ")
if answer == "7":
    print("Correct answer!")
    score = score + 1
else:
    print("Wrong answer! The correct answer is 7.")

answer = input("4. Which keyword is used to define a function in Python? ").lower()
if answer == "def":
    print("Correct answer!")
    score = score + 1
else:
    print("Wrong answer! The correct answer is def.")

answer = input("5. What is 5 + 3? ")
if answer == "8":
    print("Correct answer!")
    score = score + 1
else:
    print("Wrong answer! The correct answer is 8.")
# Calculate percentage
percentage = (score / 5) * 100
# Display quiz result
print("\n--- Quiz Result ---")
print("Your score:", score, "out of 5")
print("Percentage:", percentage, "%")
# Display performance
if percentage >= 80:
    print("Excellent!")
elif percentage >= 60:
    print("Good!")
else:
    print("Keep Practicing!")
