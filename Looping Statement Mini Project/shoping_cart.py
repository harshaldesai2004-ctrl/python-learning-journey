
# Shopping Cart Total
products = int(input("Enter number of products: "))
total_bill = 0
# Get price and quantity for each product
for i in range(1, products + 1):
    print("\nProduct", i)
    price = float(input("Enter product price: ₹"))
    quantity = int(input("Enter product quantity: "))
    # Calculate the cost of this product
    product_total = price * quantity
    # Add the product cost to the bill
    total_bill = total_bill + product_total
# Calculate discount
if total_bill >= 3000:
    discount = total_bill * 10 / 100
else:
    discount = 0
# Calculate bill after discount
amount = total_bill - discount
# Calculate delivery charges
if amount < 1500:
    delivery_charge = 100
else:
    delivery_charge = 0
# Calculate final amount
final_amount = amount + delivery_charge
# Display the bill
print("\n--- Shopping Bill ---")
print("Subtotal: ₹", round(total_bill, 2))
print("Discount: ₹", round(discount, 2))
print("Delivery Charge: ₹", delivery_charge)
print("Final Amount: ₹", round(final_amount, 2))
