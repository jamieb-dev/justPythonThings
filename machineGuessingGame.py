#! /opt/homebrew/bin/python3
import random
import time

print("Think of a number but don't tell me.")
time.sleep(1)

guess = 10

attempts = 0
    

while True:
    attempts += 1
    strAttempts = str(attempts)
    r = random.randint(1,5)
    strGuess = str(guess)
    print("Is it " + strGuess + "?")
    response = input("Yes or no?: ")
    if response.lower() == "yes":
        print("HA, you never stood a chance against me. It only took me " + strAttempts + " attempts aswell. Pfft." )
        quit()
    else:    
        with open("guesses.txt", "a") as f:
            f.write(str(guess))
            pass
        print("Hmm. Let me have another think.")
        tooHigh = input("Was I too high? Yes or no?: ")
        if tooHigh.lower() == "yes":
            guess -= r
        else:
            guess += r


# TASK: Configure temp file to store guesses on seperate lines
# TASK: Make program check for previous guesses in temp guesses.txt file
# TASK: create a tracker for guesses to avoid re-guessing the same number
# TASK: Change attempts output to make sense for a value of one (probs and if else)