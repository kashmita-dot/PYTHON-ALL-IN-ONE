# Python credit card validator program

# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left.
#        (If result is a two-digit number,
#        add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# STEP 1
card_num = input("Enter a credit card number: ")
card_num = card_num.replace("-", "").replace(" ", "")
card_num = card_num[::-1]  # Reverse the card number for easier processing
print("Card number entered: ", card_num)

# STEP 2
for x in card_num[::2]:
    sum_odd_digits += int(x)

# STEP 3
for x in card_num[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 +(x % 10))
    else:
        sum_even_digits += x

    # STEP 4
total = sum_odd_digits + sum_even_digits

# STEP 5
if total % 10 == 0:
    print("Valid credit card number")
else:
    print("Invalid credit card number")
