# Check loan application eligibility

age = int(input("Enter your age: "))
salary = float(input("Enter monthly salary: "))

# Check eligibility conditions
if age >= 21 and salary >= 15000:
    print("Eligible to apply for a loan")
else:
    print("Not eligible based on these conditions")