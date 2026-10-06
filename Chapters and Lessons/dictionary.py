# dictionary = a collection of {key:value} pairs ordered and changeable. NO duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(dir(capitals))
print(capitals.get("India"))

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.clear()

keys = capitals.keys()
for key in capitals.keys():
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")
