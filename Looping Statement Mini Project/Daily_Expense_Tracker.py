
# Daily Expense Tracker
days = int(input("Enter number of days: "))
while days <= 0:
    print("Please enter a valid number of days.")
    days = int(input("Enter number of days: "))
total = 0
highest = 0
# Enter expenses for each day
for day in range(1, days + 1):
    expense = float(input(f"Enter expense for day {day}: ₹"))
    while expense < 0:
        print("Expense cannot be negative.")
        expense = float(input(f"Enter expense for day {day}: ₹"))
    # Add expense to total
    total = total + expense
    # Find the Highest Expense
    if day == 1 or expense > highest:
        highest = expense
# Calculate average expense
average = total / days
# Display results
print("\n--- Expense Summary ---")
print(f"Total expense: ₹{total:.2f}")
print(f"Average daily expense: ₹{average:.2f}")
print(f"Highest daily expense: ₹{highest:.2f}")
# Check budget
if total > 5000:
    print("Budget Alert")
else:
    print("Budget is within ₹5,000")
