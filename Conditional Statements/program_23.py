# Calculate Electricity Bill

units = int(input("Enter units consumed: "))

# Calculate bill based on units
if units < 0:
    print("Invalid Units")
elif units <= 100:
    bill = units * 3
    print("Electricity Bill: Rs.", bill)
elif units <= 200:
    bill = (100 * 3) + ((units - 100) * 5)
    print("Electricity Bill: Rs.", bill)
else:
    bill = (100 * 3) + (100 * 5) + ((units - 200) * 7)
    print("Electricity Bill: Rs.", bill)