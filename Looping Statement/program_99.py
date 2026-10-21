# Menu-driven program using a while loop
while True:
    print("\n--- MENU ---")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 4:
        print("Program ended.")
        break
    if choice >= 1 and choice <= 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        if choice == 1:
            print("Sum =", a + b)
        elif choice == 2:
            print("Difference =", a - b)
        elif choice == 3:
            print("Product =", a * b)
    else:
        print("Invalid choice!")