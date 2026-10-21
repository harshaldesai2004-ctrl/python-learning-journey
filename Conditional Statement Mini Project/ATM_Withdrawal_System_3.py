
# ATM Withdrawal System
name = input("Enter account holder name: ")
balance = float(input("Enter current balance: ₹"))
withdrawal = float(input("Enter withdrawal amount: ₹"))

# Display Account Holder
print("\n----- ATM Transaction Details -----")
print("Account Holder:", name)

# Check withdrawal Conditions
if withdrawal <= 0:
    print("Transaction Status: Rejected")
    print("Reason: Withdrawal amount must be greater than ₹0")

elif withdrawal > balance:
    print("Transaction Status: Rejected")
    print("Reason: Insufficient account balance")

elif withdrawal > 20000:
    print("Transaction Status: Rejected")
    print("Reason: Maximum withdrawal limit is ₹20,000")

else:
    # Process withdrawal
    balance = balance - withdrawal

    print("Transaction Status: Successful")
    print("Withdrawn Amount: ₹", withdrawal)
    print("Remaining Balance: ₹", balance)

    # To check low balance
    if balance < 1000:
        print("Low Balance Warning")
    else:
        print("Balance is sufficient")
