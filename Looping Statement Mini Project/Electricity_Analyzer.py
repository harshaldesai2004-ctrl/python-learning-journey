
# Electricity Usage Analyzer
days = int(input("Enter number of days: "))
total_units = 0
high_usage_days = 0
highest_usage = 0
# Enter electricity usage for each day
for day in range(1, days + 1):
    units = float(input(f"Enter units used on day {day}: "))
    # Calculate total units
    total_units = total_units + units
    # Count days with usage above 10 units
    if units > 10:
        high_usage_days = high_usage_days + 1
    # Find the highest daily usage
    if day == 1 or units > highest_usage:
        highest_usage = units
# Calculate average usage
average_units = total_units / days
# Display the result
print("\n--- Electricity Usage Report ---")
print("Total units:", total_units)
print("Average daily units:", round(average_units, 2))
print("High usage days:", high_usage_days)
print("Highest daily usage:", highest_usage)
# Check total electricity usage
if total_units > 300:
    print("High Usage")
else:
    print("Normal Usage")
