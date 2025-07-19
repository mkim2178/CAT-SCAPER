from menus.menu import Menu
from ui import Button, Text
from constants import (
    BUTTON_DEFAULT_COLOR,
    BUTTON_HOVER_COLOR,
    FONT_TYPE,
    GAME_TITLE,
    SCREEN_WIDTH,
    TEXT_COLOR
)



class Menu_Main(Menu):

    def __init__(self, screen, screen_color):

        game_title_text = Text(GAME_TITLE, 40, TEXT_COLOR, (SCREEN_WIDTH // 2, 80), FONT_TYPE)

        
        start_button = Button((SCREEN_WIDTH // 2, 250), 180, 50, BUTTON_DEFAULT_COLOR, BUTTON_HOVER_COLOR, Text("START", 20, TEXT_COLOR, (0, 0), FONT_TYPE))
        settings_button = Button((SCREEN_WIDTH // 2, 350), 180, 50, BUTTON_DEFAULT_COLOR, BUTTON_HOVER_COLOR, Text("SETTINGS", 20, TEXT_COLOR, (0, 0), FONT_TYPE))
        credits_button = Button((SCREEN_WIDTH // 2, 450), 180, 50, BUTTON_DEFAULT_COLOR, BUTTON_HOVER_COLOR, Text("CREDITS", 20, TEXT_COLOR, (0, 0), FONT_TYPE))

        texts = [game_title_text]
        buttons = [start_button, settings_button, credits_button]

        super().__init__(screen, screen_color, texts, buttons)

        self.start_button = start_button
        self.settings_button = settings_button
        self.credits_button = credits_button

    def handle(self, event_pos):

        if self.start_button.is_clicked(event_pos):

            return "select_difficulty"

        elif self.settings_button.is_clicked(event_pos):
            return "settings"
        
        elif self.credits_button.is_clicked(event_pos):
            return "credits"
        
        return "main_menu"
        
            

