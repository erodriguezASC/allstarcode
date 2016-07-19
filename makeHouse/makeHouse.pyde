size(1000, 1000)

def makeHouse(c0lor, sIze):
    
    if c0lor == "red":
        fill(255, 0, 0)
    
    if c0lor == "blue":
        fill(0, 0, 255)
    
    if sIze == "big":
        rect(200, 200, 300, 300)
        
    if sIze == "small":
        rect(200, 200, 100, 100)
    #big roof
    if sIze == "big":
        triangle(200, 100, 200, 100, 150, 150)
    #small roof
    if sIze == "small":
        triangle(100, 100, 200, 200, 150, 150)





makeHouse("blue", "small")