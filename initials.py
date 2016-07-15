from Myro import *
init("sim")

size = int(raw_input("What size do your want your inital to be?"))
def E():
    forward(1,size)
    backward(1,size)
    turnBy(90)
    forward(1,size * 0.5)
    turnBy(-90)
    forward(1,size)
    backward(1,size)
    turnBy(90)
    forward(1,size * 0.5)
    turnBy(-90)
    forward(1,size)

def R():
    turnBy(-90)
    forward(1,size)
    backward(1,size)
    turnBy(90)
    forward(1,size*0.75)
    turnBy(-90)
    forward(1,size*0.5)
    turnBy(-90)
    forward(1,size*0.75)
    turnBy(135)
    forward(1,size*.66666)
    
def drawInitials():
    penDown()
    E()
    penUp()
    forward(1,1.5)
    penDown()
    R()
drawInitials()