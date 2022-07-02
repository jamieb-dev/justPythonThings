import random
import time
count = 0

print("You have till the count of 10!")
time.sleep(1.5)

while True:
    if count ==10:
        break
    else:  
        count += 1
        print(count, " mississippi.")
        time.sleep(1.5)

print("That's it, I warned you!")
