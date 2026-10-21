
# Smart Electricity Bill Calculator

name = input("Enter Customer Name: ")
units = float(input("Enter Units Consumed: "))

# Calculate Energy Charge
if units <= 100:
    energy_charge = units * 3
elif units <= 200:
    energy_charge = (100 * 3) + ((units - 100) * 5)
else:
    energy_charge = (100 * 3) + (100 * 5) + ((units - 200) * 7)

# Add Fixed Service Charge
service_charge = 150
final_bill = energy_charge + service_charge

# Display Bill Details
print("\n----- Electricity Bill -----")
print("Customer Name:", name)
print("Units Consumed:", units)
print("Energy Charge: ₹", energy_charge)
print("Service Charge: ₹", service_charge)
print("Final Bill: ₹", final_bill)

# Nested Condition To Check Bill Amount
if final_bill > 5000:
    print("Usage Message: High Usage Bill")
else:
    if units > 200:
        print("Usage Message: High Unit Consumption")
    else:
        print("Usage Message: Normal Usage")
