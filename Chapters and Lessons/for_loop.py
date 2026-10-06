# for lops = execute a block of code a fixed number of times.
# you can iterate over a range, strings, sequence, etc.

credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)

# break
for x in range(1,21):
    if x == 13:
        break
    else:print(x)

# continue
for x in range(1,21):
    if x == 13:
        continue
    else:print(x)