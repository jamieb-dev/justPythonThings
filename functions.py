# tutorial example
#  the two types of functions
#  1 - performs a task you've set
#  2 - calculates and returns a value

import time

#  performs a task

def greet(firstName, lastName):
    print(f"Hello, {firstName} {lastName}.")
    time.sleep(0.75)
    print("Nice to finally meet you")
    time.sleep(0.75)

greet("John", "Smith")


# calculates and returns a value
round(100/3)

# you can print it later or save it to a file

number = round(100/3)
print(number)

# my attempt
# funtion to add 2 parameters together

def add(a, b):
    a = int(a)
    b = int(b)
    return a + b

result = add(2, 4)
print(result)

# another function

# =1 after the last parameter to make only required
def getInfo(name, age, favColour):
    print(f"Hi there {name} I've heard you're {age} now. To celebrate I've got you a {favColour} jumper. It's your favourite, right?")


getInfo("Cameron", "14", "Red")