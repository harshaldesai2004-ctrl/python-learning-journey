# Calculate shopping discount

amount = float(input("Enter shopping amount: "))

# Calculate discount
if amount < 0:
    print("Invalid amount")
elif amount >= 5000:
    discount = amount * 0.20
    print("Discount:", discount)
    print("Final amount:", amount - discount)
elif amount >= 2000:
    discount = amount * 0.10
    print("Discount:", discount)
    print("Final amount:", amount - discount)
else:
    print("No discount")
    print("Final amount:", amount)