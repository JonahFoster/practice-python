# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random

number = random.randint(1, 9)
guess = int(input("Guess a number between 1 and 9: "))

if guess == number:
    print("You got it right!")
elif guess > number:
    print("Your guess was too high.")
elif number > guess:
    print("Your guess was too low.")
