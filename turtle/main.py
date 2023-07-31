import turtle

bob = turtle.Turtle()

def drawSquare():
    bob.forward(200)
    bob.left(90)
    bob.forward(200)
    bob.left(90)
    bob.forward(200)
    bob.left(90)
    bob.forward(200)

def star():
    count = 0
    bob.left(34)
    while True:
        if count == 5:
            turtle.done()
        else:
            count += 1
            bob.forward(100)
            bob.left(144)

star()

turtle.done()