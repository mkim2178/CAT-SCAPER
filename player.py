import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, screen_width, screen_height):
        super().__init__()

        # load the image to set the player's appearance -> this will be used when player's image has been selected
        self.image = pygame.image.load("images/mouse4x.png").convert_alpha()

        # get the rectangle of the image
        self.rect = self.image.get_rect(center=(320, 350))

        # set the boundaries that player can move
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.speed = 7

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:

            if self.rect.x + self.speed + self.rect.width <= self.screen_width:
                self.rect.x += self.speed
            else:
                self.rect.x = self.screen_width - self.rect.width

        if keys[pygame.K_LEFT]:

            if self.rect.x - self.speed >= 0:
                self.rect.x -= self.speed
            else:
                self.rect.x = 0
            
        if keys[pygame.K_UP]:

            if self.rect.y - self.speed >= 0:
                self.rect.y -= self.speed
            else:
                self.rect.y = 0

        if keys[pygame.K_DOWN]:

            if self.rect.y + self.speed + self.rect.height <= self.screen_height:
                self.rect.y += self.speed
            else:
                self.rect.y = self.screen_height - self.rect.height

    
    def is_collide(self, enemy):
        return self.rect.colliderect(enemy)

    def reset(self):
        self.rect.center = (320, 350)