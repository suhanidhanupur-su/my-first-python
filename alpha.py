# Guess the Number Game

import random

secret = random.randint(1, 50)

print("Guess the number between 1 and 50!")

while True:
    guess = int(input("Your guess: "))

    if guess == secret:
        print("🎉 Correct! You guessed the number!")
        break
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")