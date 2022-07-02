import random

tally = 0
count = 0
while True:
    r = random.randint(0,1)
    # print(r)
    if count == 100:
        print("Reached 5")
        quit()
    elif count == -100:
        print("Reached -5")
        quit()
    else:
        pass        
    if r == 1:
        tally += 1
        continue
    elif r == 0:
        tally -= 1
        continue



