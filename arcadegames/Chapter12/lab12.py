"""
Pygame base template for opening a window, done with functions

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""

import pygame
import random

# The use of the main function is described in Chapter 9.

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
NUMBER_OF_SHAPES = 500  # 500*2 = 1000 shapes (2 for loops)


# Create class Rectangle
class Rectangle():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.height = 0
        self.width = 0
        self.change_x = 0
        self.change_y = 0
        self.color = [0, 255, 0]

    def draw(self, screen):
        """Method creates a green 10x10 rectangle at location stored in
        self.x and self.y. Use screen reference to draw to correct screen"""
        pygame.draw.rect(
            screen, self.color, [self.x, self.y, self.width, self.height])

    def move(self):
        """Method adjusts x and y based on change_x and change_y"""
        self.x += self.change_x
        self.y += self.change_y


# Create class Ellipse
class Ellipse(Rectangle):

    def draw(self, screen):
        """Draw ellipse(Surface, color, Rect, width=0) -> Rect"""
        pygame.draw.ellipse(
            screen, self.color, [self.x, self.y, self.width, self.height])


def main():
    """ Main function for the game. """
    pygame.init()

    # Set the width and height of the screen [width,height]
    size = [700, 500]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Create and display a list of objects
    my_list = []
    # Loop through 10 times, and create 10 objects
    for i in range(NUMBER_OF_SHAPES):
        # Create variable my_object and set equal to new instance of Rectangle
        my_object = Rectangle()
        my_object.x = random.randrange(0, 700)
        my_object.y = random.randrange(0, 500)
        my_object.width = random.randrange(20, 70)
        my_object.height = random.randrange(20, 70)
        my_object.change_x = random.randrange(-3, 3)
        my_object.change_y = random.randrange(-3, 3)
        my_object.color = [random.randrange(0, 255), random.randrange(
            0, 255), random.randrange(0, 255)]
        my_list.append(my_object)

    # Create for loop that adds 10 instances of Ellipse
    for i in range(NUMBER_OF_SHAPES):
        my_object = Ellipse()
        my_object.x = random.randrange(0, 700)
        my_object.y = random.randrange(0, 500)
        my_object.width = random.randrange(20, 70)
        my_object.height = random.randrange(20, 70)
        my_object.change_x = random.randrange(-3, 3)
        my_object.change_y = random.randrange(-3, 3)
        my_object.color = [random.randrange(0, 255), random.randrange(
            0, 255), random.randrange(0, 255)]
        my_list.append(my_object)

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(BLACK)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        for i in range(len(my_list)):
            my_list[i].draw(screen)
            my_list[i].move()

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()


if __name__ == "__main__":
    main()
