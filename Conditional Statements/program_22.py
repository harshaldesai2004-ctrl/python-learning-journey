# Calculate salary bonus

salary = float(input("Enter your Salary: "))
years = int(input("Enter Years of Service: "))

# Check years of service
if years >= 5:
    bonus = salary * 0.10
    print("Bonus Amount:", bonus)
else:
    print("No Bonus")