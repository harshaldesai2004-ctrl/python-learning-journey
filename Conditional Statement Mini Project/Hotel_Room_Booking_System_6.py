
# Hotel Room Booking System
guest_name = input("Enter Guest Name: ")
room_type = input("Enter room Type (Standard, Deluxe, Suite): ")
nights = int(input("Enter Number Of Nights: "))

# Initial values
room_price = 0
discount_percentage = 0

# Validating Number Of Nights
if nights <= 0:
    print("Error: Number of nights must be greater than 0.")

else:
    # Checking room type using nested conditions
    if room_type.lower() == "standard":
        room_price = 2000
    elif room_type.lower() == "deluxe":
        room_price = 3500
    elif room_type.lower() == "suite":
        room_price = 6000
    else:
        print("Error: Invalid room type.")

    # Calculating booking amount if room type is valid
    if room_price > 0:
        room_charge = room_price * nights

        # Checking discount conditions
        if nights >= 10:
            discount_percentage = 20
        elif nights >= 5:
            discount_percentage = 10
        else:
            discount_percentage = 0

        # Calculating discount and final amount
        discount = room_charge * discount_percentage / 100
        final_amount = room_charge - discount

        # Displaying booking details
        print("\n--- Hotel Booking Details ---")
        print("Guest Name:", guest_name)
        print("Room Type:", room_type.title())
        print("Number of Nights:", nights)
        print("Room Charge: Rs.", room_charge)
        print("Discount:", discount_percentage, "%")
        print("Discount Amount: Rs.", discount)
        print("Final Booking Amount: Rs.", final_amount)
