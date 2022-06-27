#!/usr/bin/env python

import random

def main():
    """Start a element guessing game."""
    print("Guess the element!")

    data_elements = [
        "titanium",
        "Carbon",
        "Nitrogen",
        "Oxygen",
        "Silver",
        "Sodium",
        "Radium"
        ]

    x = random.choice(data_elements)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("What element am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess)) 
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main() 