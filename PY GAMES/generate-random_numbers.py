import random


low = 1
high = 100
options = ("rock","paper","scissors")
cards = ["2","3","4","5","6","7","8","9","10","J","O","K","A"]

number = random.randint(low, high)
number = random.random()
option = random.choice(options)
random.shuffle(cards)
print(cards)

# Number guessing game
low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f"Enter a number between {low} - {high}: "))
    guesses += 1

    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else:
        print(f"{guess} is correct!")
        break

print(f"This round took you {guesses} guesses")


# 2 number gussing game

lowest = 1
highest = 100
answer = random.randint(lowest, highest)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest} and {highest}")

while is_running:
    guess = input("Enetr your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest or guess > highest:
            print("That number is out of range")
            print(f"Please select a number between {lowest} and {highest}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False

    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest} and {highest}")