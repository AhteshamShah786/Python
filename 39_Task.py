# 39.	Write a program to create a guess the number game, where the user has to guess a randomly generated number.

import random

number_to_guess = random.randint(1, 100)
guess = None

while guess != number_to_guess:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")

print("Congratulations! You guessed it right.")
