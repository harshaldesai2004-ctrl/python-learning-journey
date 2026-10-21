
# Restaurant Bill Calculator

# Taking customer details
name = input("Enter Customer Name: ")
bill = float(input("Enter Food Bill Amount: "))
member = input("Are You a Member? (Yes/No): ")

# Initial values
discount = 0
service_charge = 0

# Checking Bill Amount And Membership
if bill < 0:
    print("Invalid bill amount!")

elif member.lower() != "yes" and member.lower() != "no":
    print("Invalid membership status!")

else:
    # Calculating discount based on bill amount
    if bill < 1000:
        discount = 0
    elif bill < 3000:
        discount = bill * 5 / 100
    elif bill < 5000:
        discount = bill * 10 / 100
    else:
        discount = bill * 15 / 100

    # Giving extra discount to members
    if member.lower() == "yes":
        discount = discount + (bill * 5 / 100)

    # Calculating bill after discount
    amount = bill - discount

    # Adding 5% service charge after discount
    service_charge = amount * 5 / 100
    final_bill = amount + service_charge

    # Displaying the bill
    print("\n--- Restaurant Bill ---")
    print("Customer Name:", name)
    print("Original Bill: Rs.", bill)
    print("Total Discount: Rs.", discount)
    print("Service Charge: Rs.", service_charge)
    print("Final Payable Amount: Rs.", final_bill)

    # Displaying customer message
    if final_bill >= 5000:
        print("Thank you for being a valued Customer")
    else:
        print("Thank you for visiting our Restaurant")
