# *args = allows you to psaa multiple non-key arguments
# **kwargs = allows you to pass multiple keyboard-arguments
#           * unpacking operator
#           1. Positional, 2. Default, 3. Keyboard, 4. Arbitrary

# *ARGS
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1, 2, 3, 4))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr.", "spongebob", "harold", "squarpants")

# **KWARGS
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key:10}: {value}")

print_address(street="123 Fake st.",
            city="Detroit",
                state="MI",
                zip="567890")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('pobox')}")
    print(f"{kwargs.get('city')}")
    print(f"{kwargs.get('state')}")
    print(f"{kwargs.get('zip')}")

shipping_label("Dr.", "spongebob", "squarpants", "III",
            street="123 Fake st.",
            pobox="po box #100",
            city="Detroit",
            state="MI",
            zip="567890")

