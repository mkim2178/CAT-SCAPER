from menus.menu import Menu
from ui import Button, Text
from constants import (
    BUTTON_DEFAULT_COLOR,
    BUTTON_HOVER_COLOR,
    FONT_TYPE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    TEXT_COLOR
)

class Menu_Game_Over(Menu):

    def __init__(self, screen, screen_color):

        game_over_text = Text("GAME OVER", 40, TEXT_COLOR, (SCREEN_WIDTH // 2, 80), FONT_TYPE)
        restart_button = Button((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 180, 50, BUTTON_DEFAULT_COLOR,BUTTON_HOVER_COLOR, Text("RESTART", 20, TEXT_COLOR, (0, 0), FONT_TYPE))

        texts = [game_over_text]
        buttons = [restart_button]

        super().__init__(screen, screen_color, texts, buttons)

        self.restart_button = restart_button


    def handle(self, event_pos, player, active_enemies, all_sprites):

        player.reset()
        for active_enemy in active_enemies:
            active_enemy.reset()
        all_sprites.empty()
            

        if self.restart_button.is_clicked(event_pos):
            return "select_difficulty", []

        else:
            return "game_over", active_enemies
        
    
    