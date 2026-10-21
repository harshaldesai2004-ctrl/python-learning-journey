# Simple ATM menu

balance = 5000

print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = int(input("Enter your choice (1-4): "))

# Match ATM choice
match choice:
    case 1:
        print("Your balance is Rs.", balance)

    case 2:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance = balance + amount
            print("Amount deposited successfully")
            print("New balance:", balance)
        else:
            print("Invalid amount")

    case 3:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Invalid amount")
        elif amount <= balance:
            balance = balance - amount
            print("Please collect your cash")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance")

    case 4:
        print("Thank you for using ATM")

    case _:
        print("Invalid choice")