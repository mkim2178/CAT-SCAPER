import pygame
from player import Player
from enemy import Enemy
from text import Text
from button import Button

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BG_COLOR = (48, 48, 48)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    game_over = False

    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
    enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)






    restart_text = Text("Restart", 36, (0, 0, 0), (0, 0))
    restart_button = Button((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 180, 50, (255, 255, 255), restart_text, (0, 255, 0))



    all_sprites = pygame.sprite.Group()
    all_sprites.add(player, enemy)
    for sprite in all_sprites:
        print(sprite)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    restart_button.is_clicked(event.pos)
                    print("CLICK")
                    game_over = False
                    player.reset()
                    enemy.reset()
                

            


        

        if game_over:

            screen.fill((0, 0, 0))
            restart_button.draw(screen)


            # restart with r_key
            # text_surface = font.render("Game Over! Press R to restart.", True, (255, 0, 0))
            # text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            # screen.blit(text_surface, text_rect)


            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_r]:

        
        else:

            all_sprites.update()

            # if there is a collide, game is over
            if player.rect.colliderect(enemy):
                game_over = True

            screen.fill(BG_COLOR)
            all_sprites.draw(screen)



        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()