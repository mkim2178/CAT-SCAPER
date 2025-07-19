import pygame
from entities import Player
from entities import Enemy
from ui import Survival_Timer
from menus import (
    Menu,
    Menu_Credits,
    Menu_Main,
    Menu_Settings,
    Menu_Difficulty,
    Menu_Game_Over,
    Menu_Paused
)
from constants import (
    BACKGROUND_COLOR,
    BACKGROUND_MUSIC,
    CLICK_SOUND,
    COLLIDE_SOUND,
    GAME_ICON,
    GAME_TITLE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)


class Game:

    def __init__(self):

        # initialize pygame and mixer
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()


        # bgm
        self.bgm = pygame.mixer.music
        self.bgm.load(BACKGROUND_MUSIC)
        self.bgm.set_volume(0.1)
        self.bgm.play(-1)


        # sfx
        self.click_sound = pygame.mixer.Sound(CLICK_SOUND)
        self.click_sound.set_volume(0.2)

        self.collide_sound = pygame.mixer.Sound(COLLIDE_SOUND)
        self.collide_sound.set_volume(0.2)


        # game screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)


        # game icon
        self.icon = pygame.image.load(GAME_ICON)
        pygame.display.set_icon(self.icon)


        # clock for limiting fps
        self.clock = pygame.time.Clock()
        

        # a boolean variable for the core while loop
        self.running = True


        # current game status (game starts from the main menu)
        self.game_status = "main_menu"



        # player
        self.player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

        # enemies
        self.enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.enemy2 = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.enemy3 = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)


        """
        every menu screen for each of game status
        """

        # main menu
        self.main_menu = Menu_Main(self.screen, BACKGROUND_COLOR)


        # settings menu
        self.settings_menu = Menu_Settings(self.screen, BACKGROUND_COLOR)



        # credits menu
        self.credits_menu = Menu_Credits(self.screen, BACKGROUND_COLOR)


        # difficulty selection menu
        self.select_difficulty_menu = Menu_Difficulty(self.screen, BACKGROUND_COLOR)



        # game active
        self.background_screen = Menu(self.screen, BACKGROUND_COLOR, None, None)
        self.paused_menu = Menu_Paused(self.screen, BACKGROUND_COLOR)
        self.survival_timer = Survival_Timer(self.screen)

        # game over
        self.game_over_menu = Menu_Game_Over(self.screen, BACKGROUND_COLOR)

        # active enemies
        self.active_enemies = []

        # group of sprites
        self.all_sprites = pygame.sprite.Group()




    def run(self):

        while self.running:

            self.handle_events()

            self.handle_game_status()

            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
    











    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_p and self.game_status == "game_start" or self.game_status == "pause":
                    self.game_status = self.paused_menu.handle()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                self.click_sound.play()

                if self.game_status == "main_menu":
                    self.game_status = self.main_menu.handle(event.pos)
            

                elif self.game_status == "settings":
                    self.game_status = self.settings_menu.handle(event.pos, self.bgm, [self.click_sound, self.collide_sound])


                elif self.game_status == "credits":
                    self.game_status = self.credits_menu.handle(event.pos)


                elif self.game_status == "select_difficulty":
                    self.game_status, self.active_enemies = self.select_difficulty_menu.handle(event.pos, [self.player, self.enemy, self.enemy2, self.enemy3], self.all_sprites)
                    self.survival_timer.reset_timer()
                    

                elif self.game_status == "game_over":
                    self.game_status, self.active_enemies = self.game_over_menu.handle(event.pos, self.player, self.active_enemies, self.all_sprites)
                    self.select_difficulty_menu.reset_difficulty()
                    




    def handle_game_status(self):

        
        if self.game_status == "main_menu":
            self.main_menu.fill()

        elif self.game_status == "settings":
            self.settings_menu.fill()

        elif self.game_status == "credits":
            self.credits_menu.fill()

        
        elif self.game_status == "select_difficulty":
            self.select_difficulty_menu.fill()

        elif self.game_status == "game_start":
            
            self.background_screen.fill()

            self.all_sprites.update()

            for active_enemy in self.active_enemies:
                if self.player.is_collide(active_enemy):
                    self.collide_sound.play()
                    self.game_status = "game_over"
                    break

            self.all_sprites.draw(self.screen)

            self.survival_timer.start_timer()


        elif self.game_status == "pause":
            self.paused_menu.fill()
            self.survival_timer.pause_timer()


        elif self.game_status == "game_over":
            self.game_over_menu.fill()
            self.survival_timer.pause_timer()
