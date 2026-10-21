# Check ticket price based on age

age = int(input("Enter your age: "))

# Calculate ticket price
if age < 12:
    print("Ticket price: Rs. 50")
elif age < 60:
    print("Ticket price: Rs. 100")
else:
    print("Ticket price: Rs. 70")