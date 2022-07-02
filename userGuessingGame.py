import random

while True:
    topRange = input("Enter a number. ")
    if topRange.isdigit():
        topRange = int(topRange)
        break

    else:
        print("Enter a digit next time. ")
        continue

r = random.randint(0, topRange)
attempts = 0

while True:
    guess = input("Guess the random number: ")
    if guess.isdigit():
        guess = int(guess)
        attempts += 1
        if guess < r:
            print("Too low")
            
            continue
        elif guess == r:
            print("Correct!")
            break
        else:
            print("Too high.")
            continue
    else:
        print("That's not a number, try again.")
        continue

if attempts == 1:
    print("You guessed it in ", attempts, " attempt. Well done!")
else:
    attempts = str(attempts)
    print("You got it in " + attempts + " attempts. Good effort.")
    