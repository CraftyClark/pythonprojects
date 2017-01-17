"""
 Shooter Game
 Andrew Clark
"""
import pygame
import random
import constants


# --- Classes
class Block(pygame.sprite.Sprite):
    """ This class represents the block. """

    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([20, 15])
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1

        if self.rect.y > (constants.SCREEN_HEIGHT + 15):
            self.lose_life()

    def lose_life(self):
        self.block_list.remove(self.block)
        self.all_sprites_list.remove(self.block)
        print("ouch")


class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """

    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([20, 20])
        self.image.fill(constants.RED)

        self.rect = self.image.get_rect()

    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()

        # Set the player x position to the mouse x position
        self.rect.x = pos[0]


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([4, 10])
        self.image.fill(constants.BLACK)

        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3


class Game(object):
    """ This class represents an instance of the game. If we need to reset the
        game, we'd just need to create a new instance of this class. """

    def __init__(self):
        """ Constructor. Create all our attributes and initialize the game. """

        self.score = 0
        self.game_over = False

        # --- Sprite lists
        # This is a list of every sprite. All blocks & the player block as well
        self.all_sprites_list = pygame.sprite.Group()

        # List of each block in the game
        self.block_list = pygame.sprite.Group()

        # List of each bullet
        self.bullet_list = pygame.sprite.Group()

        # --- Create the sprites

        for i in range(50):
            # This represents a block
            block = Block(constants.BLUE)

            # Set a random location for the block
            block.rect.x = random.randrange(constants.SCREEN_WIDTH)
            block.rect.y = random.randrange(350)

            # Add the block to the list of objects
            self.block_list.add(block)
            self.all_sprites_list.add(block)

        # Create a red player block
        self.player = Player()
        self.all_sprites_list.add(self.player)
        self.player.rect.y = 370

    def process_events(self):
        """ Process all of the events. Return a "True" if we need to close
            the window. """

        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Fire a bullet if the user clicks the mouse button
                bullet = Bullet()
                # Set the bullet so it is where the player is
                bullet.rect.x = self.player.rect.x
                bullet.rect.y = self.player.rect.y
                # Add the bullet to the lists
                self.all_sprites_list.add(bullet)
                self.bullet_list.add(bullet)
                if self.game_over:
                    self.__init__()
        return False

    def run_logic(self):
        """ This method is run each time through the frame. It updates
            positions and checks for collisions. """
        if not self.game_over:
            # Call the update() method on all the sprites
            self.all_sprites_list.update()

            # Calculate mechanics for each bullet
            for bullet in self.bullet_list:

                # See if it hit a block
                block_hit_list = pygame.sprite.spritecollide(
                    bullet, self.block_list, True)

                # For each block hit, remove the bullet and add to the score
                for block in block_hit_list:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                    self.score += 1
                    print(self.score)

                # Remove the bullet if it flies up off the screen
                if bullet.rect.y < -10:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)

    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        # Clear the screen
        screen.fill(constants.WHITE)

        if self.game_over:
            # font = pygame.font.Font("Serif", 25)
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, click to restart",
                               True, constants.BLACK)
            center_x = (constants.SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (constants.SCREEN_HEIGHT // 2) - \
                (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        if not self.game_over:
            # Draw all the spites
            self.all_sprites_list.draw(screen)
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()


def main():
    """Main program function. """
    # Initialize Pygame
    pygame.init()

    # Set the height and width of the screen
    screen = pygame.display.set_mode(
        [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])

    pygame.display.set_caption("My Game")
    pygame.mouse.set_visible(False)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Create an instance of the Game class
    game = Game()

    # -------- Main Program Loop -----------
    while not done:

        # Process events (keystrokes, mouseclicks, etc)
        done = game.process_events()

        # Update object positions, check for collisions
        game.run_logic()

        # Draw the current frame
        game.display_frame(screen)

        # --- Limit to 20 frames per second
        clock.tick(60)

    pygame.quit()


# Call the main function, start up the game
if __name__ == "__main__":
    main()
