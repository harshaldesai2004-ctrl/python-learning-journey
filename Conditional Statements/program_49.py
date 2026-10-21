# Print result status

status = input("Enter result status (pass/fail/absent): ").lower()

# Match result status
match status:
    case "pass":
        print("Congratulations! You passed.")
    case "fail":
        print("You failed.")
    case "absent":
        print("You were absent.")
    case _:
        print("Invalid result status")