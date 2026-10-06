# formate specifiers = {value:flags} format a value based on what flags are inserted

price1 = 30000.141253
price2 = -9870.643853
price3 = 12000.88

# round decimals
print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")

# padding
print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")

# justify
print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

# justify ceneterd
print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")

# comma seperater
print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")

# mix and match format
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:-,.2f}")
print(f"Price 3 is ${price3:+,.2f}")

