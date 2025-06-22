import pygame
import random
import math

class Enemy(pygame.sprite.Sprite):

    def __init__(self, screen_width, screen_height):
        super().__init__()

        # load the image to set the player's appearance -> this will be used when player's image has been selected
        self.image = pygame.image.load("images/cat4x.png").convert_alpha()

        # get the rectangle of the image
        self.rect = self.image.get_rect(center=(960, 350))

        # set the boundaries that player can move
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.speed = 5
        self.max_speed = 15

        
        self.direction = self.starting_direction()

        self.dx = math.cos(self.direction)
        self.dy = math.sin(self.direction)

    
    def starting_direction(self):

        ranges = [
            (25, 65),
            (115, 155),
            (205, 245),
            (295, 335)
        ]

        random_range = random.choice(ranges)
        degree = random.uniform(*random_range)
        radian_value = math.radians(degree)

        return radian_value
    

    def update(self):

        self.rect.x += self.dx * self.speed
        self.rect.y += self.dy * self.speed

        if self.rect.x <= 0 or self.rect.x + self.rect.width >= self.screen_width:
            self.dx *= -1
            self.speed += 1
            self.speed = min(self.speed, self.max_speed)

        
        if self.rect.y <= 0 or self.rect.y + self.rect.height >= self.screen_height:
            self.dy *= -1
            self.speed += 1
            self.speed = min(self.speed, self.max_speed)

    
    def reset(self):
        self.rect = self.image.get_rect(center=(960, 350))
        self.speed = 5
        self.direction = self.starting_direction()
        self.dx = math.cos(self.direction)
        self.dy = math.sin(self.direction)