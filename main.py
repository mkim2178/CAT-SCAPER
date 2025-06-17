import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
PLAYER_SIZE = 20
PLAYER_SPEED = 10
PLAYER_COLOR = (30, 30, 30)
BG_COLOR = (245, 245, 245)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    player = pygame.Rect(
        (SCREEN_WIDTH - PLAYER_SIZE) // 2,
        (SCREEN_HEIGHT - PLAYER_SIZE) // 2,
        PLAYER_SIZE,
        PLAYER_SIZE
    )

    while running:


        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            #     PLAYER_COLOR = (220, 220, 220)
            #     BG_COLOR = (30, 30, 30)

                
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            player.move_ip(PLAYER_SPEED, 0)
        if keys[pygame.K_LEFT]:
            player.move_ip(-PLAYER_SPEED, 0)
        if keys[pygame.K_UP]:
            player.move_ip(0, -PLAYER_SPEED)
        if keys[pygame.K_DOWN]:
            player.move_ip(0, PLAYER_SPEED)

        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, PLAYER_COLOR, player)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()