# Generator = Function that behaves like an iterator (it can be used in a for loop)
#             Pauses a function, returns a value, then resumes
#             Uses 'yield' instead or 'return'
#             Iterate without loading everything into memory (ex. reading large files)
#             return = Pouring bucket
#             yield = Drip faucet

# EX 1
def count_to(n):
    count = 1
    while count <= n:
        yield count
        count+=1

number = int(input("Enter a number to count to: "))
for n in count_to(number):
    print(n)

# EX 2  E:\PYTHON
def read_file(file_path):
    with open(file_path) as file:
        for line in file:
            yield line.strip()

file_path = "E:\\PYTHON\\test2.txt"

for line in read_file(file_path):
    print(line)

