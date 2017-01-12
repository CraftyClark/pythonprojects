"""
 Animating multiple objects using a list.
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/Gkhz3FuhGoI
"""
 
# Import a library of functions called 'pygame'
import pygame
import random
 
# Initialize the game engine
pygame.init()
 
COLORS = [(139, 0, 0), 
          (0, 100, 0),
          (0, 0, 139)]

def random_color():
    return random.choice(COLORS)

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = (255, 0, 0)
new_color = WHITE 
direction = " "
# Set the height and width of the screen
SIZE = [400, 400]
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Hungry Snake")
 
# Create an empty array
snake_list = []
 
# Loop 50 times and add a snow flake in a random x,y position
x = random.randrange(0, 380)
y = random.randrange(0, 380)
snake_list.append([x, y])
 
# Create food rectangle
food_x = random.randrange(0, 380)
food_y = random.randrange(0, 380)

clock = pygame.time.Clock()
 
# Loop until the user clicks the close button.
done = False

snake_x = 20
while not done:
 
    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop
 
    # Set the screen background
    screen.fill(BLACK)
    # Process each snow flake in the list
    for i in range(len(snake_list)):
        
        # Draw the snow flake
        pygame.draw.rect(screen, new_color, [snake_list[i], [snake_x, 20]])
        pygame.draw.rect(screen, RED, [food_x, food_y, 20, 20])

        # Move snake to eat food
        if snake_list[0][1] < food_y:
             snake_list[0][1] += 1
        elif snake_list[0][1] > food_y:
            snake_list[0][1] -= 1

        if snake_list[0][1] == food_y:
            if snake_list[0][0] < food_x:
                snake_list[0][0] += 1
                direction = "RIGHT"
            elif snake_list[0][0] > food_x:
                snake_list[0][0] -= 1
                direction = "LEFT"
            else:
                #Snake has found food, append another 20x20 rectangle to snake
                #snake_list.append([food_x, food_y])
                # Create food rectangle
                food_x = random.randrange(0, 380)
                food_y = random.randrange(0, 380)
                #if direction == "RIGHT":
                snake_x += 20
                new_color = random_color()
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(20)
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()