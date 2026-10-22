
# ATM PIN Verification
# Set the correct ATM PIN
correct_pin = "1234"
attempts = 0
# Give the user 3 chances to enter the PIN
while attempts < 3:
    pin = input("Enter your ATM PIN: ")
    attempts = attempts + 1
    # Check whether the PIN is correct
    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("Incorrect PIN. Please try again.")
# Display the number of attempts
print("Attempts used:", attempts)
# Check whether the card should be locked
if pin != correct_pin:
    print("Card Temporarily Locked")
