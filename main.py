import pygame
from screen import Screen
from player import Player
from enemy import Enemy
from text import Text
from button import Button

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
GAME_TITLE = "CAT-SCAPER"
GAME_ICON = pygame.image.load("images\mouse4x.png")  # Your icon image path
FONT_TYPE = "fonts\PressStart2P-Regular.ttf"
BG_COLOR = (31, 41, 55)
TEXT_COLOR = (230, 230, 230)
BUTTON_DEFAULT_COLOR = (59, 89, 152)
BUTTON_HOVER_COLOR = (84, 127, 206)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    pygame.display.set_caption(GAME_TITLE)
    pygame.display.set_icon(GAME_ICON)

    clock = pygame.time.Clock()
    running = True


    # game_status = [ "pause_menu", game_over, game_start, settings_menu, stats_menu, credits]
    
    game_status = "main_menu"


    """
    Starting menu buttons: start, settings, credits


    game start -> game_status = game_on (start the game)
    pause the game: pause menu buttons: continue (continue the game), settings (setttings menu buttons (set background sound, set sound effect sound, go back button (go back to the pause menu))), quit (game_over, go back to the menu)
    game over -> show the total score and game over menu buttons: restart, stats,
    game restart -> reset the previous score and restart the game
    stats -> type box to type user name and confirm it -> show the stats and restart button
    """


    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
    enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
    enemy2 = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
    enemy3 = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)




    """
    starting_menu = Screen(screen, BG_COLOR, [game_title], [start_button, settings_button, credits_button])
    """


    """
    ------------------------------------------------------STARTING MENU------------------------------------------------------
    """
    game_title_text = Text(GAME_TITLE, 40, TEXT_COLOR, (SCREEN_WIDTH // 2, 80), FONT_TYPE)

    start_text = Text("Start", 20, TEXT_COLOR, (0, 0), FONT_TYPE)
    start_button = Button((SCREEN_WIDTH // 2, 300), 180, 50, BUTTON_DEFAULT_COLOR, BUTTON_HOVER_COLOR, start_text)

    settings_text = Text("Settings", 20, TEXT_COLOR, (0, 0), FONT_TYPE)
    settings_button =  Button((SCREEN_WIDTH // 2, 400), 180, 50, BUTTON_DEFAULT_COLOR, BUTTON_HOVER_COLOR, settings_text)

    credits_text = Text("Credits", 20, TEXT_COLOR, (0, 0), FONT_TYPE)
    credits_button = Button((SCREEN_WIDTH // 2, 500), 180, 50, BUTTON_DEFAULT_COLOR, BUTTON_HOVER_COLOR, credits_text)

    starting_menu = Screen(screen, BG_COLOR, [game_title_text], [start_button, settings_button, credits_button])

    background_screen = Screen(screen, BG_COLOR, None, None)
    """
    ------------------------------------------------------STARTING MENU------------------------------------------------------
    """




    """
    ------------------------------------------------DIFFICULTY SELECTION MENU------------------------------------------------
    """
    difficulty_selected = False

    difficulty_text = Text("SELECT DIFFICULTY", 40, TEXT_COLOR, (SCREEN_WIDTH // 2, 80), FONT_TYPE)

    easy_text = Text("EASY", 20, TEXT_COLOR, (0, 0), FONT_TYPE)
    easy_button = Button((SCREEN_WIDTH // 2, 300), 180, 50, BUTTON_DEFAULT_COLOR, BUTTON_HOVER_COLOR, easy_text)

    normal_text = Text("NORMAL", 20, TEXT_COLOR, (0, 0), FONT_TYPE)
    normal_button =  Button((SCREEN_WIDTH // 2, 400), 180, 50, BUTTON_DEFAULT_COLOR, BUTTON_HOVER_COLOR, normal_text)

    hard_text = Text("HARD", 20, TEXT_COLOR, (0, 0), FONT_TYPE)
    hard_button = Button((SCREEN_WIDTH // 2, 500), 180, 50, BUTTON_DEFAULT_COLOR, BUTTON_HOVER_COLOR, hard_text)

    selecting_difficulty_menu = Screen(screen, BG_COLOR, [difficulty_text], [easy_button, normal_button, hard_button])
    """
    ------------------------------------------------DIFFICULTY SELECTION MENU------------------------------------------------
    """





    """
    -----------------------------------------------------GAME OVER MENU-----------------------------------------------------
    """
    game_over_text = Text("Game Over", 40, TEXT_COLOR, (SCREEN_WIDTH // 2, 80), FONT_TYPE)
    restart_text = Text("Restart", 20, TEXT_COLOR, (0, 0), FONT_TYPE)
    restart_button = Button((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 180, 50, (59, 130, 246),(37, 99, 235), restart_text)

    restarting_menu = Screen(screen, BG_COLOR, [game_over_text], [restart_button])
    """
    -----------------------------------------------------GAME OVER MENU-----------------------------------------------------
    """






    active_enemies = []
    all_sprites = pygame.sprite.Group()
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

                    if game_status == "main_menu":

                        if start_button.is_clicked(event.pos):
                            print("SELECT DIFFICULTY")
                            game_status = "select_difficulty"
                    
                    elif game_status == "select_difficulty":

                        if not difficulty_selected:
                            
                            if easy_button.is_clicked(event.pos):
                                print("DIFFICULTY: EASY")
                                active_enemies = [enemy]
                                all_sprites.add(player, enemy)
                                difficulty_selected = True
                                game_status = "game_start"
                        
                            elif normal_button.is_clicked(event.pos):
                                print("DIFFICULTY: NORMAL")
                                active_enemies = [enemy, enemy2]
                                all_sprites.add(player, enemy, enemy2)
                                difficulty_selected = True
                                game_status = "game_start"
                    
                            elif hard_button.is_clicked(event.pos):
                                print("DIFFICULTY: HARD")
                                active_enemies = [enemy, enemy2, enemy3]
                                all_sprites.add(player, enemy, enemy2, enemy3)
                                difficulty_selected = True
                                game_status = "game_start"
                            
                            else:
                                pass
                        
        
                    elif game_status == "game_over":

                        if restart_button.is_clicked(event.pos):
                            print("GAME RESTART! SELECT DIFFICULTY")
                            game_status = "select_difficulty"
                            player.reset()
                            for active_enemy in active_enemies:
                                active_enemy.reset()
                            all_sprites.empty()
                            active_enemies = []
                            difficulty_selected = False
                

            
        if game_status == "main_menu":
            starting_menu.fill()
        
        elif game_status == "select_difficulty":
            selecting_difficulty_menu.fill()

        elif game_status == "game_start":
            
            background_screen.fill()

            all_sprites.update()

            # if there is a collide, game is over
            for active_enemy in active_enemies:
                if player.is_collide(active_enemy):
                    game_status = "game_over"
                    break

            all_sprites.draw(screen)
        
        elif game_status == "game_over":
            restarting_menu.fill()



        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()