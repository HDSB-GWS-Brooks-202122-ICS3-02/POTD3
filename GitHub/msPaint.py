import pygame

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))
    mainSurface.fill((255, 255, 255))
    

    # Set up some data to describe a small circle and its color
    RED = pygame.Color(255,0,0)
    GREEN = pygame.Color(0,255,0)
    BLUE = pygame.Color(0,0,255)
    WHITE = pygame.Color(255, 255, 255)
    
    circleColor = RED        # A color is a mix of (Red, Green, Blue)
    circleX = 200;
    circleY = 200;
    
  

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        elif ev.type == pygame.MOUSEBUTTONUP:
            if ev.button == 3:
                drawCircle = False
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 3:
                drawCircle = True
            #if circleColor == (255, 0, 0):
                #circleColor = (0, 0, 255)
            #elif circleColor == (0, 0, 255):
                #circleColor = (255, 0, 0)
        elif ev.type == pygame.MOUSEMOTION:
            circleX = ev.pos[0]
            circleY = ev.pos[1]
            


        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        #mainSurface.fill((0, 200, 255))

               
        # Draw a circle on the surface
        pygame.draw.circle(mainSurface, circleColor, (circleX,circleY), 7.5)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

main()