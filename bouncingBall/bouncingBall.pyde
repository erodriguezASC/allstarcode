from time import sleep
from random import *
a = randrange(25, 475)
b = randrange(25, 475)
xCoordinate= b
yCoordinate= a
c= choice([-5,-2,2,5])
xv = c
yv = c

def setup():
    size(500, 500)
    background(255, 255, 255)

def draw():
    #moves ball straight down
    global xCoordinate, yCoordinate, yv, xv

    
    background(255, 255, 255)
    fill(0, 255, 0)
    noStroke()
    ellipse(xCoordinate, yCoordinate, 50, 50)
    yCoordinate = yCoordinate + yv
    xCoordinate = xCoordinate + xv
    
    #Paddle
    fill(0, 0, 0)
    rect(mouseX - 40, 450, 80, 20)
    if (mouseX - 80 < xCoordinate < mouseX + 40) and (yCoordinate > 430):
        yv = yv*-1
    
    #bottom of screen and top of screen
    if yCoordinate > 475 or yCoordinate < 25:
        yv = yv*-1
    
    #right part of screen and left part of screen
    if xCoordinate > 475 or xCoordinate < 25:
        xv = xv*-1
   
    
        
     
    
        

        