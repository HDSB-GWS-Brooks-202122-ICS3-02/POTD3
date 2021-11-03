import pygame

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))
    
    

    # Set up some data to describe a small circle and its color
    RED = pygame.Color(255,0,0)
    GREEN = pygame.Color(0,255,0)
    BLUE = pygame.Color(0,0,255)
    BLACK = pygame.Color(0, 0, 0)
    BROWN = pygame.Color(125, 99, 29)
    BROWN2 = pygame.Color(185, 145, 40)
    
    fps = 60
    clock = pygame.time.Clock()
    
    circleX = 2000;
    circleY = 2000;
    circleColor = RED
    ballDropped = False
    bottom = 470
    circleSize = 8
    fallingSpeed = 0.01
    
    
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        mainSurface.fill((0, 200, 255))
    
        pygame.draw.rect(mainSurface, BROWN, pygame.Rect(150, 50, 320, 420))
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
        
        if (ballDropped == False) and (ev.type == pygame.MOUSEBUTTONDOWN):
            circleX = ev.pos[0]
            circleY = ev.pos[1]
            ballDropped = True
            
        circleY += fallingSpeed
        
        if ((circleY + circleSize) > bottom) and (ballDropped == True):
            circleY = bottom - circleSize
            fallingSpeed = 0
        else:
            circleY += 0.38
            
        pygame.draw.circle(mainSurface, circleColor, (circleX,circleY), 8)

            

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.
    clock.tick(fps)
main()