import _tkinter
import turtle

win = turtle.Screen()
win.title("Pong")
win.bgcolor("orange")
win.setup(width=800, height=600)
win.tracer(0)

# MAIN LOOP

while True:
    win.update()


# left paddle

PADDLE_A = turtle.Turtle()
PADDLE_A.speed(0)
PADDLE_A.shape("square")
PADDLE_A.color("blue")
PADDLE_A.penup()
PADDLE_A.goto(-350, 0)

