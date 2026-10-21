
# Insurance Premium Calculator

# Taking customer details
name = input("Enter Customer Name: ")
age = int(input("Enter Age: "))
occupation = input("Enter occupation risk (Low/Medium/High): ")
smoker = input("Are You a Smoker? (Yes/No): ")

# Setting base premium
base_premium = 10000
additional_charges = 0

# Checking eligibility
if age < 18:
    print("Sorry, you are not eligible for insurance.")

elif (occupation.lower() != "low" and
      occupation.lower() != "medium" and
      occupation.lower() != "high"):
    print("Invalid occupation risk!")

elif smoker.lower() != "yes" and smoker.lower() != "no":
    print("Invalid smoking status!")

else:
    # Checking age condition
    if age > 50:
        additional_charges = additional_charges + 5000

    # Checking occupation risk
    if occupation.lower() == "high":
        additional_charges = additional_charges + 7000
    elif occupation.lower() == "medium":
        additional_charges = additional_charges + 3000

    # Checking smoking status
    if smoker.lower() == "yes":
        additional_charges = additional_charges + 5000

    # Calculating final premium
    final_premium = base_premium + additional_charges

    # Checking policy risk
    if additional_charges >= 10000:
        risk_message = "High Risk Policy"
    else:
        risk_message = "Normal Risk Policy"

    # Displaying Insurance Details
    print("\n--- Insurance Premium Details ---")
    print("Customer Name:", name)
    print("Eligibility: Eligible")
    print("Base Premium: Rs.", base_premium)
    print("Additional Charges: Rs.", additional_charges)
    print("Final Premium: Rs.", final_premium)
    print("Risk Message:", risk_message)
