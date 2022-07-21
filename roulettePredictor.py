import random

c = random.randint(0,1)
n = random.randint(0,1)

if c == 0:
    colour = "black"
else:
    colour = "red"

if n == 0:
    number = "even"
else:
    number = "odd"

print("colour: " + colour)
print("number: " + number)

if 