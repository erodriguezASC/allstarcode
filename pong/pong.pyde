from time import sleep
from random import *

a = randrange(25, 475)
b = randrange(25, 475)
xCoordinate= b
yCoordinate= a
c= choice([-5,5])
xv = c
yv = c
score = 0

def setup():
    size(500, 500)
    background(255, 255, 255)
    frameRate(60)

def draw():
    
    global xCoordinate, yCoordinate, yv, xv, score
    #spawns ball in random place
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
    
    #Second Paddle controlled by computer
    fill(0, 0, 0)
    rect(xCoordinate - 40, 50, 80, 20)
    if yCoordinate < 85:
        yv = yv*-1
    
    #bottom of screen 
    if yCoordinate > 475:
        score = score + 1
        print score
        #background(0, 0, 0)
        # fill(255, 0, 0)
        # textSize(100)
        # text("YOU LOSE", 10, 250)
    
    #top of screen
    if yCoordinate < 25:
        yv = yv*-1
    
    #right part of screen and left part of screen
    if xCoordinate > 475 or xCoordinate < 25:
        xv = xv*-1
   
 
        
     
    
        

        