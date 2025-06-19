import pygame
import random

PLAYER_SIZE = 30
PLAYER_SPEED = 10

class Player(pygame.sprite.Sprite):

    def __init__(self, screen_width, screen_height):
        super().__init__()

        # load the image to set the player's appearance -> this will be used when player's image has been selected
        # self.image = pygame.image.load("bat_optimized.png").convert_alpha()

        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill((30, 30, 30))

        # get the rectangle of the image
        self.rect = self.image.get_rect()
        
        # set the player's starting point
        self.rect.topleft = (random.randint(0, screen_width - PLAYER_SIZE), random.randint(0, screen_height - PLAYER_SIZE))

        # set the boundaries that player can move
        self.x_max_boundary = screen_width - PLAYER_SIZE
        self.y_max_boundary = screen_height - PLAYER_SIZE

        

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:

            if self.rect.left + PLAYER_SIZE <= self.x_max_boundary:
                self.rect.left += PLAYER_SPEED
            else:
                self.rect.left = self.x_max_boundary

        if keys[pygame.K_LEFT]:

            if self.rect.left - PLAYER_SIZE >= 0:
                self.rect.left -= PLAYER_SPEED
            else:
                self.rect.left = 0

            
        if keys[pygame.K_UP]:

            if self.rect.top - PLAYER_SIZE >= 0:
                self.rect.top -= PLAYER_SPEED
            else:
                self.rect.top = 0

        if keys[pygame.K_DOWN]:

            if self.rect.top + PLAYER_SIZE <= self.y_max_boundary:
                self.rect.top += PLAYER_SPEED
            else:
                self.rect.top = self.y_max_boundary
        





    def test_random_starting_points(self):

        for i in range(100):

            x = random.randint(0, 1260)
            y = random.randint(0, 700)

            if x < 0 or x > 1260:
                print(f"WRONG X_POS: {x}")
            if y < 0 or y > 700:
                print(f"WRONG Y_POS: {y}")
            if 0 <= x <= 1260 and 0 <= y <= 700:
                print(f"CORRECT X AND Y: {x, y}")