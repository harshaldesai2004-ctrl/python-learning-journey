
# Number Guessing Game
secret_number = 37
attempts = 0
# Give the user 5 chances
while attempts < 5:
    guess = int(input("Guess the number: "))
    attempts = attempts + 1
    # Check the user's guess
    if guess == secret_number:
        print("Congratulations! You guessed correctly.")
        break
    elif guess < secret_number:
        print("Too low! Try a bigger number.")
    else:
        print("Too high! Try a smaller number.")
# Display total attempts
print("Attempts used:", attempts)
# Check whether the user won
if guess != secret_number:
    print("You lost!")
    print("The secret number was:", secret_number)
