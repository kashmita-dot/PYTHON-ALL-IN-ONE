# MEMBERSHIP OPERATIONS = used to test whether a value or variable is found in a sequence 
#                       (string, list, tuple, set, or dictionary)
#                       1. IN
#                       2. NOT IN


# EX 1
word = "APPLE"
letter = input("Guess a letter in the secret word: ").upper()
if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"There is a {letter}")

# EX 2
students = {"alex", "john", "mike", "sarah"}
student = input("Enter a student name: ").lower()
if student not in students:
    print(f"{student} is not in the class")
else:
    print(f"{student} is in the class")


# EX 3
grades = {"alex": 90, "john": 85, "mike": 78, "sarah": 92}
student = input("Enter a student name: ").lower()
if student in grades:
    print(f"{student} has a grade of {grades[student]}")
else:
    print(f"{student} is not in the system")    

# EX 4 
email = "kashie@gmail.com"

if "@" in email and "." in email:
    print("Valid email address")
else:
    print("Invalid email address")

