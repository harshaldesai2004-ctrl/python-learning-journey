
# Movie Ticket Booking System

# Taking Customer Details
name = input("Enter customer name: ")
age = int(input("Enter age: "))
show = input("Enter show type (Morning/Evening): ")
day = input("Enter day type (Weekday/Weekend): ")

# Setting ticket price
price = 200
discount = 0
surcharge = 0

# Checking age and other inputs
if age < 0:
    print("Invalid age!")

elif show.lower() != "morning" and show.lower() != "evening":
    print("Invalid show type!")

elif day.lower() != "weekday" and day.lower() != "weekend":
    print("Invalid day type!")

else:
    # Checking Age-based Discount
    if age < 12:
        discount = 100
    elif age >= 60:
        discount = 60
    else:
        discount = 0

    # Checking morning show discount
    if show.lower() == "morning":
        discount = discount + 30

    # Checking weekend surcharge
    if day.lower() == "weekend":
        surcharge = 50

    # Calculating final ticket price
    final_price = price - discount + surcharge

    # Displaying Booking Details
    print("\n--- Movie Ticket Details ---")
    print("Customer Name:", name)
    print("Original Ticket Price: Rs.", price)
    print("Discount: Rs.", discount)
    print("Weekend Surcharge: Rs.", surcharge)
    print("Final Ticket Price: Rs.", final_price)
