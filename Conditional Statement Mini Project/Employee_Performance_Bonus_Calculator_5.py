
# Employee Performance Bonus Calculator

name = input("Enter Employee Name: ")
salary = float(input("Enter Monthly salary: "))
experience = int(input("Enter Years Of Experience: "))
rating = int(input("Enter Performance Rating (1-5): "))

# Initial values
bonus_percentage = 0
performance_message = "Good Performance"

# Checking Whether Rating Is Valid
if rating < 1 or rating > 5:
    print("Invalid rating! Please enter a rating between 1 and 5.")

# Checking Bonus Conditions
else:
    if rating == 5:
        performance_message = "Excellent Performer"
    elif rating >= 3:
        performance_message = "Good Performance"
    else:
        performance_message = "Needs Improvement"

    if experience >= 10 and rating >= 4:
        bonus_percentage = 20
    elif experience >= 5 and rating >= 4:
        bonus_percentage = 15
    elif experience >= 2 and rating >= 3:
        bonus_percentage = 10
    elif rating < 3:
        bonus_percentage = 0
    else:
        bonus_percentage = 0

    # Calculating Bonus Amount And Final Salary
    bonus_amount = salary * bonus_percentage / 100
    final_salary = salary + bonus_amount

    # Displaying The Result
    print("\n--- Employee Bonus Details ---")
    print("Employee Name:", name)
    print("Bonus Percentage:", bonus_percentage, "%")
    print("Bonus Amount: Rs.", bonus_amount)
    print("Final Salary: Rs.", final_salary)
    print("Performance Message:", performance_message)
