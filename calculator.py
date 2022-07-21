def add(a, b):
    return a + b

def times(a, b):
    return a + b

def div():
    return a / b

def sub():
    return a - b

options = ["add", "sub", "times", "sub"]
while True:
    print("Pick an option...")
    mode = input("add, sub, times, div. (q to quit): ")
    if mode == "add":
        intOne = int(input("Enter a starting number: "))
        intTwo = int(input("Enter a second number: "))
        print(intOne + intTwo)
    elif mode == "sub":
        intOne = int(input("Enter a starting number: "))
        intTwo = int(input("Enter a second number: "))
        print(intOne - intTwo)
    elif mode == "times":
        intOne = int(input("Enter a starting number: "))
        intTwo = int(input("Enter a second number: "))
        print(intOne * intTwo)
    elif mode == "div":
        intOne = int(input("Enter a starting number: "))
        intTwo = int(input("Enter a second number: "))
        print(intOne / intTwo)
    elif mode == "q":
        quit()
    else:
        print("Invalid mode")
        continue