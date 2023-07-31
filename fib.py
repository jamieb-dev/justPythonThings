import time



def fib():
    global x, y
    z = x + y
    print(y)
    x = y
    y = z
    z = x + y
    # time.sleep(0.1)

x = 0
y = 1

while True:
    if len(str(y)) < 160:
        fib()
    else:
        quit()