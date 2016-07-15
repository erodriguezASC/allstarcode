from Myro import *
init("sim")

i = 0 
speed = 1

while i < 2:
    forward(speed, .5)
    backward(speed, .5)
    i = i + 1
    while i < 2:
        turnBy(5)
        turnBy(-10)
        i = i + 1
        while i < 2:
            motors(1,0,.5)
            motors(1,0,1)
            i = i + 1