import pygame
import sys
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each grid location # This sets the margin between each cell

WIDTH =0
HEIGHT = 0
MARGIN = 0
 
bSize = 0

# Loop until the user clicks the close button.
done = False
clock = 0
screen = 0




def initPygame(bSize):
    
    global clock
    global screen
    # Initialize pygame
    
    global WIDTH
    global HEIGHT 
    global MARGIN 
    
    WIDTH = math.floor(750/bSize)+1
    HEIGHT = math.floor(750/bSize)+1
    MARGIN = math.floor(300/bSize)
    pygame.init()
    
 
    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE =[(WIDTH+MARGIN)*bSize+MARGIN,(WIDTH+MARGIN)*bSize+MARGIN]
    print( WIDTH,MARGIN,WINDOW_SIZE)

    screen = pygame.display.set_mode(WINDOW_SIZE)
    # Set title of screen
    pygame.display.set_caption("Life simulator")
    clock = pygame.time.Clock()
     
    # Used to manage how fast the screen updates
 

def updateUI(grid,bSize):
    screen.fill(BLACK)
    
    # Draw the grid
    for row in range(bSize):
        for column in range(bSize):
            color = WHITE
            
            if (type(grid[row][column]) == int):
                color = (0,min(math.sqrt(grid[row][column])*2, 255), 0)
                
            elif(grid[row][column].alive):
                val=min(math.sqrt(grid[row][column].foodlevel)*2+50,255)
                if(grid[row][column].kind=="herbivore"):
                    color = (0,0,val)
                
                elif(grid[row][column].kind=="carnivore"):
                    color = (val,0,0)
                    
                elif(grid[row][column].kind=="omnivore"):
                    color = (val,0,val)
    
                elif(grid[row][column].kind=="angel"):
                    color = (min(grid[row][column].foodlevel+5, 255),min(grid[row][column].foodlevel+5, 255),min(grid[row][column].foodlevel+5, 255))
                else:
                    print("wtf is that ? UI")
                

            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
def terminateUI():
    pygame.quit()
    sys.exit()
    
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
if __name__ == '__main__':
    pygame.quit()
    sys.exit()
