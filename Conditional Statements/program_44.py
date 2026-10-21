# Traffic signal instructions

signal = input("Enter traffic signal (red/yellow/green): ").lower()

# Match traffic signal
match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid signal")