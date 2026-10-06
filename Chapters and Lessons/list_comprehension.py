# List comprehension = A concise way to create lists in python
#                     Compact and easier to read than traditional loops
#                     [expression for value in iterable if condition]

# EX 1
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)
print(doubles)

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

print(doubles)
print(triples)
print(squares)

# EX 2
fruits = [fruit.upper() for fruit in ["apple", "banana", "cherry", "kiwi", "mango"]]
print(fruits)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)

# EX 3
numbers = [1, -2, 3, -4, -5, -6]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num <= 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 != 0]
print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

# EX 4
grades = [90, 25, 67, 45, 80]
passed = [grade for grade in grades if grade >= 60]
failed = [grade for grade in grades if grade < 60]
print(passed)
print(failed)