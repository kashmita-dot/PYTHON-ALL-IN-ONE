# KEYBOARD ARGUMENTS = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. Positional, 2. Default, 3. Keyboard, 4. Arbitrary


# EXAMPLE 1
def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("HELLO", title="Mr.", last="John", first="James")

# Example 2
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)

print(phone_num)

