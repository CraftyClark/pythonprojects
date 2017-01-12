import pygame


class Ball():
    def __init__(self):
        # --- Class Attributes ---
        # Ball position
        self.x = 0
        self.y = 0

        # Ball's vector
        self.change_x = 0
        self.change_y = 0

        # Ball size
        self.size = 10

        # Ball color
        self.color = [255, 255, 255]

    # --- Class Methods ---
    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)

    theBall = Ball()
    theBall.x = 100
    theBall.y = 100
    theBall.change_x = 2
    theBall.change_y = 1
    theBall.color = [255,0,0]


