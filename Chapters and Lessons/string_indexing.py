# indexing = accessing elements of a sequence using [] (indexing operation)
# [start : end : step]

credit_number = "1234-5678-9012-9996"
print(credit_number[0])
print(credit_number[0:6])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-1])
print(credit_number[::3])


last_digits = credit_number[-4:]
credit_number = credit_number[::-1]
print(credit_number)