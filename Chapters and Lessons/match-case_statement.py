# Match-case statement (switch): An alternative to using many 'elif staements
#                              Execute some code if a value matches a 'case
#                              Benefits: cleaner and syntax is more readable

# METHOD 1
def day_of_week(day):
        match day:
            case 1:
                return "It is sunday"
            case 2:
                return "It is monday"
            case 3:
                return "It is tuesday"
            case 4:
                return "It is wednesday"
            case 5:
                return "It is thursday"
            case 6:
                return "It is friday"
            case 7:
                return "It is saturday"
            case _:
                return "Not a valid day"

print(day_of_week())

# METHOD 2
def is_weekend(day):
        match day:
            case "sunday":
                return True
            case "monday":
                return False
            case "tuesday":
                return False
            case "wednesday":
                return False
            case "thursday":
                return False
            case "friday":
                return False
            case "saturday":
                return True
            case _:
                return False

print(is_weekend("monday"))

# METHOD 3
# using | , or
def is_weekend(day):
        match day:
            case "saturday" | "sunday":
                return True
            case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
                return False
            case _:
                return False

print(is_weekend("sunday"))
