"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("Welcome to thaa game")
    print("enter a number plz")
    lower_number = False
    while not lower_number:
        lower = input("Enter a lower number: ")
        try:
            lower = int(lower)
            print(f"A number between {lower_number} and _ ?")
            lower_number = True
        except:
            print("enter a REAL number")
    higher_number = False
    while not higher_number:
        higher = input("Enter a higher number: ")
        try:
            higher = int(higher)
            if lower < higher:
                print(f"Enter a number between {lower} and {higher}")
                higher = True
            elif lower > higher:
                print("I need a larger number")
            elif lower == higher:
                print("numbers are the same, enter again")
        except:
            print("enter a REAL number")

    actualNumber = random.randint(lower, higher)

    guessed = False

    while not guessed:
        try:
            guessedNumber = input("Guess a number: ")
            guessedNumber = int(guessedNumber)
            print("You guessed {},".format(guessedNumber),)
            if guessedNumber == actualNumber:
                print("You got it!! It was {}".format(actualNumber))
                guessed = True
            elif guessedNumber < actualNumber:
                print("Too small, try again :'(")
            else:
                print("Too big, try again :'(")
        except:
            print("{} thats not a number!!!! Give me a number!!!".format(guessedNumber))
    return "You got it!"


    # the tests are looking for the exact string "You got it!". Don't modify that!
if __name__ == "__main__":
    print(advancedGuessingGame())
