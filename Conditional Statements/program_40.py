# Check password using nested if

password = input("Enter password: ")

# Check password length
if len(password) >= 8:
    # Check whether password contains spaces
    if " " not in password:
        print("Valid password")
    else:
        print("Password must not contain spaces")
else:
    print("Password must contain at least 8 characters")