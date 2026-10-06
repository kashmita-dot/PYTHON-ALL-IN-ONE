# Generator Expression = Similar to a list comprehension but uses () instead of []
#                        Creates a generator (iterator) that yields values one at a time
#                        No need to define a function or use yield
#                        Less flexible than a gen func and not reusable
#                       gen object = (expression for value in iterable if condition)

# COUNT NUMBER USING GEN
number = int(input("Enter a number to count uo to: "))

counter = (count for count in range(1, number + 1))

for n in counter:
    print(n)

# READING A FILE UNSING GEN
file_path = "E:\\PYTHON\\test2.txt"

with open(file_path) as file:
    lines = (line.strip() for line in file)
    for line in lines:
        print(line)


# ADDING IF CONDITION, GENERATE NUMBER
number = int(input("ENter a number to square up to: "))

even_squares = (x**2 for x in range(1, number + 1 ) if x % 2 == 0)

for square in even_squares:
    print(square)