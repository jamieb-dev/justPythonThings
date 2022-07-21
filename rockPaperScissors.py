import random

user = 0
machine = 0

options = ["rock", "paper", "scissors"]


while True:
    if user == 3:
        print("Well done, you beat the computer.")
        break
    elif machine == 3:
        print("Oh no, you lost. Better luck next time.")
        break
    else:
        print(str(user) + " - " + str(machine))    
        userGo = input("Rock, Paper or Scissors: ").lower()
        r = random.randint(0, 2)
        machineGo = options[r]
        if userGo == machineGo:
            print("That's a draw.")
        elif userGo == "rock" and machineGo == "paper":
            machine += 1
            print("You lose.")
        elif userGo == "rock" and machineGo == "scissors":
            user += 1
            print("You win.")
        elif userGo == "paper" and machineGo == "scissors":
            machine += 1
            print("You lose.")
        elif userGo == "paper" and machineGo == "rock":
            user += 1
            print("You win.")
        elif userGo == "scissors" and machineGo == "rock":
            machine +=1
            print("You lose.")
        elif userGo == "scissors" and machineGo == "paper":
            user += 1
            print("You win.")

        else:
            print(oops)
        
print("End of game.")


    # TASK: Find a way of eliminating the global variables
    # TASK: Add option to try again in event of typo