
#Online Shopping Checkout

# Input details
name = input("Enter customer name: ")
amount = float(input("Enter purchase amount: "))
customer_type = input("Enter customer type (Regular/Premium): ").strip().lower()

# Calculate discount based on purchase amount
if amount >= 5000:
    discount_rate = 0.20
elif amount >= 3000 and amount < 5000:
    discount_rate = 0.10
elif amount >= 1000 and amount < 3000:
    discount_rate = 0.05
else:
    discount_rate = 0

# Calculate discount amount
discount = amount * discount_rate

# Additional discount for Premium customers
if customer_type == "premium":
    extra_discount = amount * 0.05
    discount = discount + extra_discount

# Ensure Total Discount Does Not Exceed Purchase Amount
if discount > amount:
    discount = amount

# Calculate Amount After Discount
amount_after_discount = amount - discount

# Calculate Delivery Charge 
if amount_after_discount >= 2000:
    delivery_charge = 0
else:
    if customer_type == "premium" or amount_after_discount < 2000:
        delivery_charge = 100

# Calculate Final Amount
final_amount = amount_after_discount + delivery_charge

#Checkout Details
print("\n----- Online Shopping Checkout -----")
print("Customer Name:", name)
print("Customer Type:", customer_type.title())
print("Purchase Amount: ₹", amount)
print("Discount Amount: ₹", discount)
print("Delivery Charge: ₹", delivery_charge)
print("Final Payable Amount: ₹", final_amount)
