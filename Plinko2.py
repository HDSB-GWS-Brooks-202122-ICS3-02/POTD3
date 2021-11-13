import pygame

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))
    
    

    # Set variables for colors to be used later on
    RED = pygame.Color(255,0,0)
    GREEN = pygame.Color(0,255,0)
    BLUE = pygame.Color(0,0,255)
    BLACK = pygame.Color(0, 0, 0)
    BROWN = pygame.Color(125, 99, 29)
    BROWN2 = pygame.Color(185, 145, 40)
    
    fps = 60
    clock = pygame.time.Clock() #Set a frames per second so that it runs at a steady pace
    
    circleX = 2000; #Spawn a ball WAY off the screen since we don't want it but we need the code later
    circleY = 2000;
    circleColor = RED
    ballDropped = False  #Variables to be used for gravity physics later on
    bottom = 470
    circleSize = 8
    fallingSpeed = 0.01
    
    font = pygame.font.SysFont("Comic Sans MS", 18) #Get a font and size ready for the rules later
    
    counter3 = 0
    hitCircleLeft = False
    hitCircleRight = False
    
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        mainSurface.fill((0, 200, 255))
    
        pygame.draw.rect(mainSurface, BROWN, pygame.Rect(150, 50, 320, 420)) #All these shapes are what make up the plinko board itself
        pygame.draw.rect(mainSurface, BROWN2, pygame.Rect(150, 390, 320, 80))
        pygame.draw.line(mainSurface, BLACK, (150,50), (150,470))
        pygame.draw.line(mainSurface, BLACK, (470, 50), (470,470))
        pygame.draw.line(mainSurface, BLACK, (150, 470), (470,470))
        pygame.draw.line(mainSurface, BLACK, (205, 390), (205,470))
        pygame.draw.line(mainSurface, BLACK, (260, 390), (260,470))
        pygame.draw.line(mainSurface, BLACK, (315, 390), (315,470))
        pygame.draw.line(mainSurface, BLACK, (370, 390), (370,470))
        pygame.draw.line(mainSurface, BLACK, (425, 390), (425,470))
        pygame.draw.line(mainSurface, BLACK, (480, 390), (480,470))
        pygame.draw.circle(mainSurface, BROWN2, (315, 320), 20)
        pygame.draw.circle(mainSurface, BROWN2, (215, 300), 20)
        pygame.draw.circle(mainSurface, BROWN2, (415, 300), 20)
        pygame.draw.circle(mainSurface, BROWN2, (315, 220), 20)
        pygame.draw.circle(mainSurface, BROWN2, (430, 220), 20)
        pygame.draw.circle(mainSurface, BROWN2, (190, 220), 20)
        pygame.draw.circle(mainSurface, BROWN2, (260, 160), 20)
        pygame.draw.circle(mainSurface, BROWN2, (370, 160), 20)
        pygame.draw.circle(mainSurface, BROWN2, (315, 100), 20)
        pygame.draw.circle(mainSurface, BROWN2, (430, 100), 20)
        pygame.draw.circle(mainSurface, BROWN2, (190, 100), 20)
        
        line = font.render('Here are the rules. ', 1, BLACK) #Selecting color and what to say
        line2 = font.render('You must drop a', 1, BLACK)
        line3 = font.render('ball into one of', 1, BLACK)
        line4 = font.render('the columns that', 1, BLACK)
        line5 = font.render('says win to win.', 1, BLACK)
        line6 = font.render('Easy.', 1, (0,0,0))
        mainSurface.blit(line, (10,0)) #Blit-ing font code above to the main surface (what everything is on)
        mainSurface.blit(line2, (10,20))
        mainSurface.blit(line3, (10,40))
        mainSurface.blit(line4, (10,60))
        mainSurface.blit(line5, (10,80))
        mainSurface.blit(line6, (10,120))
        
        if (ballDropped == False) and (ev.type == pygame.MOUSEBUTTONDOWN): #If a ball hasn't been dropped yet and you clicked drop a ball and set ballDropped to true (so you can't drop another)
            circleX = ev.pos[0]
            circleY = ev.pos[1]
            ballDropped = True
            
        #circleY += fallingSpeed
        
        if ((circleY + circleSize) > bottom) and (ballDropped == True): #if the circle hasn't touched the bottom decrease height
            circleY = bottom - circleSize
            fallingSpeed = 0
        else:
            circleY += 0.32 #speed at which the ball falls
            
        pygame.draw.circle(mainSurface, circleColor, (circleX,circleY), 8) #drawing a circle with gravity mechanics

        if ((circleX >= 295) and (circleX < 315)) and ((circleY > 300) and (circleY < 340)):
            hitCircleLeft = True 
        elif ((circleX >= 315) and (circleX <= 335)) and ((circleY > 300) and (circleY < 340)):
            hitCircleRight = True
        if ((circleX >= 195) and (circleX < 215)) and ((circleY >280) and (circleY < 320)):
            hitCircleLeft = True 
        elif ((circleX >= 215) and (circleX <= 235)) and ((circleY > 280) and (circleY < 320)):
            hitCircleRight = True
        if ((circleX >= 395) and (circleX < 415)) and ((circleY >280) and (circleY < 320)):
            hitCircleLeft = True 
        elif ((circleX >= 415) and (circleX <= 435)) and ((circleY > 280) and (circleY < 320)):
            hitCircleRight = True
        if ((circleX >= 295) and (circleX < 315)) and ((circleY >200) and (circleY < 240)):
            hitCircleLeft = True 
        elif ((circleX >= 315) and (circleX <= 335)) and ((circleY > 200) and (circleY < 240)):
            hitCircleRight = True
        if ((circleX >= 410) and (circleX < 430)) and ((circleY >200) and (circleY < 240)):
            hitCircleLeft = True 
        elif ((circleX >= 430) and (circleX <= 450)) and ((circleY > 200) and (circleY < 240)):
            hitCircleRight = True
        if ((circleX >= 170) and (circleX < 190)) and ((circleY >200) and (circleY < 240)):
            hitCircleLeft = True 
        elif ((circleX >= 190) and (circleX <= 210)) and ((circleY > 200) and (circleY < 240)):
            hitCircleRight = True
        if ((circleX >= 240) and (circleX < 260)) and ((circleY >140) and (circleY < 180)):
            hitCircleLeft = True 
        elif ((circleX >= 260) and (circleX <= 280)) and ((circleY > 140) and (circleY < 180)):
            hitCircleRight = True
        if ((circleX >= 350) and (circleX < 370)) and ((circleY >140) and (circleY < 180)):
            hitCircleLeft = True 
        elif ((circleX >= 370) and (circleX <= 390)) and ((circleY > 140) and (circleY < 180)):
            hitCircleRight = True
        if ((circleX >= 295) and (circleX < 315)) and ((circleY >80) and (circleY < 120)):
            hitCircleLeft = True 
        elif ((circleX >= 315) and (circleX <= 335)) and ((circleY > 80) and (circleY < 120)):
            hitCircleRight = True
        if ((circleX >= 410) and (circleX < 430)) and ((circleY >80) and (circleY < 120)):
            hitCircleLeft = True 
        elif ((circleX >= 430) and (circleX <= 450)) and ((circleY > 80) and (circleY < 120)):
            hitCircleRight = True
        if ((circleX >= 170) and (circleX < 190)) and ((circleY >80) and (circleY < 120)):
            hitCircleLeft = True 
        elif ((circleX >= 190) and (circleX <= 210)) and ((circleY > 80) and (circleY < 120)):
            hitCircleRight = True
            
        if (circleX <= 150) and (circleX >= 140):
            circleX += 15
        if (circleX <= 480) and (circleX >= 470):
            circleX -= 15
            
        if hitCircleRight == True:
            counter3 += 1
            if (counter3 > 0) and (counter3 < 80):
                circleX += 0.5
                circleY += 0.4    
        elif hitCircleLeft == True:
            counter3 += 1
            if (counter3 > 0) and (counter3 < 80):
                circleX -= 0.5
                circleY += 0.4
                
        if counter3 > 80:
            hitCircleLeft = False
            hitCircleRight = False
            counter3 = 0
            

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.
    clock.tick(fps)
main()
