# collection = single "variable" used to store multiple values
# LIST = [] ordered and changeable, Duplicates OK
# SET = {} unordered and imutable, but Add/remove OK, NO duplicates
# TUPLE = () ordered and unchangeable, duplicates OK, FASTER

fruits = ["apple", "orange", "banana","coconut"]             #list
fruits = {"apple", "orange", "banana","coconut","coconut"}     #set
fruits = ("apple", "orange", "banana","coconut","coconut")     #tuple
print(fruits[2])

print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("apple" in fruits)  #true (bool)
print("lichi" in fruits)   #False (bool)
fruits[1] = "pineapple"
fruits.append("pineaplle")
fruits.remove("apple")
fruits.insert(0, "pineapple")
fruits.sort()
fruits.reverse()
fruits.clear()
print(fruits.index("coconut"))       #tuple
print(fruits.count("coconut"))       #tuple
fruits.add("pineapple")
fruits.pop()
print(fruits)
print(fruits[0])
for fruit in fruits:
    print(fruit)