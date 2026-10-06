# and = checks two or more conditions if True
# or = checks if at least one condition is True
# not = true if condition is false, and vice versa

# AND logical operature
temp = 41

if temp > 0 and temp < 30:
    print("The temperature is good")
else:
    print("The temperature is bad")



# OR logical operator
temp = 25

if temp <= 0 or temp >= 30:
    print("The temperature is bad")
else:
    print("The temperature is good")



# NOT logical operator
temp = 25
sunny = True

if temp <= 0 or temp >= 30:
    print("The temperature is bad")
else:
    print("The temperature is good")

if not sunny:
    print("It is cloudy outside")
else:
    print("It is sunny outside")

