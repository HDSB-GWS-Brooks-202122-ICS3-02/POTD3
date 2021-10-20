import pygame
import random 

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

    circleColor = BLACK        # A color is a mix of (Red, Green, Blue)
    circleX = 200;
    circleY = 200;
    drawCircle = True
    circleSpeed = 0.1

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop



        # Update your game objects and data structures here...
        circleY = circleY + circleSpeed
        if circleY >= surfaceSize:
            circleSpeed = -random.randint(10,20)/100
            circleColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        elif circleY <=0:
            circleSpeed = -circleSpeed
            circleColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            
        circleX = circleX + circleSpeed
        if circleX >= surfaceSize:
            circleSpeed = -circleSpeed
        elif circleX <=0:
            circleSpeed = -circleSpeed
            circleColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))


        # Draw a circle on the surface
        if (drawCircle == True):
            pygame.draw.circle(mainSurface, circleColor, (circleX,circleY), 20)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

main()