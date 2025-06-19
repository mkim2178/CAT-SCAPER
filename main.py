import pygame
from player import Player

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BG_COLOR = (166, 224, 206)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
        
        # update every sprite
        all_sprites.update()

        # draw the screen
        screen.fill(BG_COLOR)

        # draw every sprite
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()