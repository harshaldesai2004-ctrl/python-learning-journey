
# Mobile Data Plan Bill Calculator

customer_name = input("Enter Customer Name: ")
plan_type = input("Enter plan type (Basic, Standard, Premium): ")
extra_data = float(input("Enter extra data used in GB: "))

# Initial values
base_charge = 0
extra_data_charge = 0
surcharge = 0

# Checking Negative Data Usage
if extra_data < 0:
    print("Error: Data usage cannot be negative.")

else:
    # Checking the selected plan
    if plan_type.lower() == "basic":
        base_charge = 299
    elif plan_type.lower() == "standard":
        base_charge = 499
    elif plan_type.lower() == "premium":
        base_charge = 799
    else:
        print("Error: Invalid plan type.")

    # Calculating additional charges if plan is valid
    if base_charge > 0:
        extra_data_charge = extra_data * 20

        # Applying surcharge
        if extra_data > 10:
            surcharge = 100
        else:
            surcharge = 0

        # Calculating Final Bill
        final_bill = base_charge + extra_data_charge + surcharge

        # Displaying Bill Details
        print("\n--- Mobile Data Bill ---")
        print("Customer Name:", customer_name)
        print("Plan Type:", plan_type.title())
        print("Base Plan Charge: Rs.", base_charge)
        print("Extra Data Charge: Rs.", extra_data_charge)
        print("Surcharge: Rs.", surcharge)
        print("Final Bill: Rs.", final_bill)
