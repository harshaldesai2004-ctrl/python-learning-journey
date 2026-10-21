# Language selection

print("1. English")
print("2. Marathi")
print("3. Hindi")

choice = int(input("Choose a language (1-3): "))

# Match language choice
match choice:
    case 1:
        print("You selected English")
    case 2:
        print("You selected Marathi")
    case 3:
        print("You selected Hindi")
    case _:
        print("Invalid choice")