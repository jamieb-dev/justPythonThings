import random
MAX_GUESSES = 10
NUM_DIGITS = 3

def main():

    print("I am thinking of a {} digit number, try to guess it.".format(MAX_GUESSES))
    print('''In order to help here are some clues:
    When I say:       I Mean:
    Pico              One digit is correct but in the wrong position
    Fermi             One digit is correct and in the right position
    Bagels            No digit is correct''')

    while True:
        secretNum = getSecretNum()
        print("I have thought of a number...")
        print("You have {} guesses to get it.".format(MAX_GUESSES))

        numGuesses = 1

        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != MAX_GUESSES or not guess.isdecimal():
                print("Guess #{}".format(guess))
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses:
                print("You ran out of guesses.")
                print("the answer was {}.".format(secretNum))

            print("Do you want to play again? (yes ot no).")
            if not input("yes"):
                break
        print("Thanks for playing.")

def getSecretNum():
    numbers = list("123456789")
    random.shuffle(numbers)
        
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum
        
def getClues(guess, secretNum):
    if guess == secretNum:
        return "You got it!"

        clues = []

        for i in range(len(guess)):
            if guess[i] == secretNum[i]:
                clues.append('Fermi')
            elif guess[i] in secretNum:
                clues.append('Pico')
        if len(clues) == 0:
            return "Bagels"
        else:
            clues.sort()
            return ''.join(clues)


main()