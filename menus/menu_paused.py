from menus.menu import Menu
from ui import Button, Text
from constants import (
    FONT_TYPE,
    SCREEN_WIDTH,
    TEXT_COLOR
)


class Menu_Paused(Menu):

    def __init__(self, screen, screen_color):

        paused_text = Text("Paused", 40, TEXT_COLOR, (SCREEN_WIDTH // 2, 80), FONT_TYPE)
        continue_text = Text("Press p to continue!", 20, TEXT_COLOR, (SCREEN_WIDTH // 2, 120), FONT_TYPE)

        texts = [paused_text, continue_text]

        super().__init__(screen, screen_color, texts, buttons=None)

        self.is_paused = False

    
    def handle(self):

        if not self.is_paused:
            self.is_paused = True
            return "pause"
        
        self.is_paused = False
        return "game_start"