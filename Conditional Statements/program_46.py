# Print grade description

grade = input("Enter grade (A, B, C, F): ").upper()

# Match grade
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade")