# python compound interest calculator
#  A = P(1+r/n)^t 
# where, 
# A = final amount, 
# P = intial principal balance, 
# r = interest rate, 
# t = number of time periods elapsed

# using while true loops
principle = 0 
rate = 0 
time = 0
while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than or equal to zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than or equal to zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}") 
