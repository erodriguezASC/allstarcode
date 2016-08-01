from random import *
#Variables
aliensAlive = 36
bulletY = 0
bulletX = 0 
isBulletFire = False
playerX = 50
r = 0
z = 0.0075
alienBulletFire = False
enemyList = [
    #[health, x, y]
    [1, 50, 50],
    [1, 100, 50],
    [1, 150, 50],
    [1, 200, 50],
    [1, 250, 50],
    [1, 300, 50],
    [1, 350, 50],
    [1, 400, 50],
    [1, 450, 50],
    [1, 50, 100],
    [1, 100, 100],
    [1, 150, 100],
    [1, 200, 100],
    [1, 250, 100],
    [1, 300, 100],
    [1, 350, 100],
    [1, 400, 100],
    [1, 450, 100],
    [1, 50, 150],
    [1, 100, 150],
    [1, 150, 150],
    [1, 200, 150],
    [1, 250, 150],
    [1, 300, 150],
    [1, 350, 150],
    [1, 400, 150],
    [1, 450, 150],
    [1, 50, 200],
    [1, 100, 200],
    [1, 150, 200],
    [1, 200, 200],
    [1, 250, 200],
    [1, 300, 200],
    [1, 350, 200],
    [1, 400, 200],
    [1, 450, 200]
]


def intersect(s1_x, s1_y, s2_x, s2_y):
  r = 10  
  if (s1_x > s2_x - r) and (s1_x < s2_x + r) and (s1_y > s2_y - r) and (s1_y < s2_y + r):
    return 1
  else:
    return 0

def setup():
    size(500, 500)
    background(255, 255, 255)

def draw():
    global enemyList, bulletY, bulletX, isBulletFire, x, y, playerX, r, z, aliensAlive, alienBulletFire, chosenOne
    
    #player
    background (0)
    rect(playerX, 450, 50, 20)
    fill(0, 255, 0)
    
    #Score
    textSize(20)
    text("Aliens Alive: "+str(aliensAlive), 10, 20 )
    fill(255, 255, 255)
    
    #Arrow key movement
    if keyPressed == True:
        if keyCode == 37:
            playerX = playerX - 3
        if keyCode == 39:
            playerX = playerX + 3
    
    #Creates borders on left and right of screen
    if playerX <= 0:
        playerX = 0
    if playerX >= 450:
        playerX = 450
    
    #Lets player shoot
    if keyPressed == True:
        if keyCode == 0 and isBulletFire == False:
            isBulletFire = True
            bulletX = playerX + 25
            bulletY = 440

    if isBulletFire == True:
        ellipse(bulletX, bulletY, 10, 10)
        bulletY = bulletY - 8
    
    if bulletY <= 0:#resets bullet after leaving screen
        isBulletFire = False
        bulletX = playerX + 25
    
    #Aliens
    for x in range(len(enemyList)):
        if enemyList[x][0] == 1:
            fill(255, 0, 0)
            ellipse(enemyList[x][1] + r, enemyList[x][2], 20, 20)
            r += z # r += x 
        #Aliens shuffle back and forth
        if enemyList[x][1] + r >= 490:
            z = -0.0075
        
        if enemyList [x][1] + r <= 10:
            z = 0.0075
           
        #Aliens die when shot
        if intersect(bulletX, bulletY, enemyList[x][1]+ r, enemyList[x][2]) and enemyList[x][0] == 1:
            enemyList[x][0] = 0
            isBulletFire = False
            aliensAlive = aliensAlive - 1
        
    # #Aliens shoot back randomly
    # alienBullet = choice(enemyList[x][1][2])
    # print alienBullet
    # #if choice(enemyList[x][0] = 1) and 
    
    

            
            
    
        
            
            
    
    
    
  


        
            
    