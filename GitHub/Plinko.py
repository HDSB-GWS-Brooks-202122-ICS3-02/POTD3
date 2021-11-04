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
    
    fps = 80
    clock = pygame.time.Clock() #Set a frames per second so that it runs at a steady pace
    
    circleX = 2000; #Spawn a ball WAY off the screen since we don't want it but we need the code later
    circleY = 2000;
    circleColor = RED
    ballDropped = False  #Variables to be used for gravity physics later on
    bottom = 470
    circleSize = 8
    fallingSpeed = 0.01
    
    font = pygame.font.SysFont("Comic Sans MS", 18) #Get a font and size ready for the rules later
    
    screenDisplayed = False
    counter = 0
    
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        
        print(screenDisplayed, counter)
        if screenDisplayed == False:
            counter += 1
            startScreen = pygame.image.load("startScreen.png")
            mainSurface.blit(startScreen, (-120,50))
            if counter > 200:
                screenDisplayed = True
        
        if screenDisplayed == True:        
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
            line6 = font.render('Click to spawn', 1, BLACK)
            line7 = font.render('the ball.', 1, BLACK)
            mainSurface.blit(line, (10,0)) #Blit-ing font code above to the main surface (what everything is on)
            mainSurface.blit(line2, (10,20))
            mainSurface.blit(line3, (10,40))
            mainSurface.blit(line4, (10,60))
            mainSurface.blit(line5, (10,80))
            mainSurface.blit(line6, (10,120))
            mainSurface.blit(line7, (10,140))
            
            if (ballDropped == False) and (ev.type == pygame.MOUSEBUTTONDOWN): #If a ball hasn't been dropped yet and you clicked drop a ball and set ballDropped to true (so you can't drop another)
                circleX = ev.pos[0]
                circleY = ev.pos[1]
                ballDropped = True
                
            #circleY += fallingSpeed
            
            if ((circleY + circleSize) > bottom) and (ballDropped == True): #if the circle hasn't touched the bottom decrease height
                circleY = bottom - circleSize
                fallingSpeed = 0
            else:
                circleY += 0.38 #speed at which the ball falls
                
            pygame.draw.circle(mainSurface, circleColor, (circleX,circleY), circleSize) #drawing a circle with gravity mechanics

                

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()     # Once we leave the loop, close the window.
    
main()
