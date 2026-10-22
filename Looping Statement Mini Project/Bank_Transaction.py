
# Bank Transaction History
balance = float(input("Enter opening balance: ₹"))

# Ask for the number of transactions
transactions = int(input("Enter number of transactions: "))
deposit_count = 0
successful_withdrawals = 0
rejected_withdrawals = 0

# Process each transaction
for i in range(1, transactions + 1):
    print("\nTransaction", i)

    transaction_type = input(
        "Enter D for Deposit or W for Withdrawal: "
    ).upper()

    amount = float(input("Enter transaction amount: ₹"))

    # Check deposit or withdrawal
    if transaction_type == "D":
        balance = balance + amount
        deposit_count = deposit_count + 1
        print("Deposit successful!")

    elif transaction_type == "W":
        # Check whether enough balance is available
        if amount <= balance:
            balance = balance - amount
            successful_withdrawals = successful_withdrawals + 1
            print("Withdrawal successful!")
        else:
            rejected_withdrawals = rejected_withdrawals + 1
            print("Withdrawal rejected: Insufficient balance.")
    else:
        print("Invalid transaction type.")
# Display account summary
print("\n--- Bank Transaction Summary ---")
print("Final Balance: ₹", round(balance, 2))
print("Total Deposits:", deposit_count)
print("Successful Withdrawals:", successful_withdrawals)
print("Rejected Withdrawals:", rejected_withdrawals)
# Check the final balance
if balance < 1000:
    print("Warning: Your balance is below ₹1,000.")
