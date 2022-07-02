# A quiz with basic python concepts

print("Would you like to take this quiz?")

playingTrue = input("Type 'yes' or 'no'.  ")
playing = playingTrue.lower()

if playing == "yes":
    pass
elif playing == "no":
    quit()
else:
    print("That wasn't an option. ")
    quit()
# TASK: Add loop function here that requests answer again

score = 0

print()
answer1 = input("Question 1: What colour is the sky?  ")
if answer1.lower() == "blue":
        print("Correct!")
        score = score + 1
        # also written as score += 1
        print("Score: ", score)
else:
    print("Incorrect!")
    print("Score = ", score)

# TASK: Add "A little higher" and "A bit lower" hints. 

print()
answer2 = input("Question 2: How many points does a traingle have?  ")
if answer2 == "3":
        print("Correct!")
        score += 1
        print("Score = ", score)
else:
    print("Incorrect!")
    print("Score = ", score)

print()
answer3 = input("Question 3: When was Back to the Future Day?  ")
if answer3 == "21.08.2015"  "21/08/2015":
    print("Correct!")
    score += 1
    print("Score = ", score)
    print
else:
    print("Incorrect!")

print()
print("Final Score.")
print("You achieved a " + str((score/3)*100) + "% accuracy.")