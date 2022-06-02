
import random

def computer_guess(x):
    low = 1
    high = x
    feedback =  ""
    while feedback != "C":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        guess = random.randint(low, high)
        feedback = input(f" Is {guess} correct? H for too high, L for too low, C for correct ").upper()
        if feedback == "H":
            high = guess - 1
        if feedback == "L":
            low = guess + 1

    print(f"The computer has correctly guessed {guess}")