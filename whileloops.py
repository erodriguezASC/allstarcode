from Myro import *
init ("sim")

i = 0 # set counter
speed = 1 
size= int(raw_input("What size do you want your square to be?"))
degrees = 90


while i < 4:
    forward (speed, size)
    turnBy(degrees)
    i=i+1