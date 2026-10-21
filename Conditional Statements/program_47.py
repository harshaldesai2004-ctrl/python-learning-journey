# Check user role

role = input("Enter role (admin/user/guest): ").lower()

# Match user role
match role:
    case "admin":
        print("Full access")
    case "user":
        print("Normal access")
    case "guest":
        print("Limited access")
    case _:
        print("Invalid role")