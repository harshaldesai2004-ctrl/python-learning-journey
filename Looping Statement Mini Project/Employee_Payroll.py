
# Employee Payroll Summary
employees = int(input("Enter number of employees: "))
total_payroll = 0
# Get details of each employee
for i in range(1, employees + 1):
    print("\nEmployee", i)
    name = input("Enter employee name: ")
    basic_salary = float(input("Enter basic salary: ₹"))
    overtime_hours = float(input("Enter overtime hours: "))
    # Calculate overtime pay
    overtime_pay = overtime_hours * 200
    # Calculate gross salary
    gross_salary = basic_salary + overtime_pay
    # Calculate salary deduction
    if gross_salary >= 50000:
        deduction = gross_salary * 10 / 100
    else:
        deduction = gross_salary * 5 / 100
    # Calculate net salary
    net_salary = gross_salary - deduction
    # Add net salary to total payroll
    total_payroll = total_payroll + net_salary
    # Display employee salary details
    print("\nEmployee Name:", name)
    print("Gross Salary: ₹", round(gross_salary, 2))
    print("Deduction: ₹", round(deduction, 2))
    print("Net Salary: ₹", round(net_salary, 2))
# Display total payroll
print("\n--- Payroll Summary ---")
print("Total Employees:", employees)
print("Total Net Payroll: ₹", round(total_payroll, 2))
