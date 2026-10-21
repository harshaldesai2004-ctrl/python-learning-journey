# Check blood donation eligibility

age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))

# Check age and weight
if age >= 18 and age <= 65 and weight >= 50:
    print("Eligible for blood donation screening")
else:
    print("Not eligible based on these conditions")