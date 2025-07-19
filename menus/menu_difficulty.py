from menus.menu import Menu
from ui import Button, Text
from constants import (
    BUTTON_DEFAULT_COLOR,
    BUTTON_HOVER_COLOR,
    FONT_TYPE,
    SCREEN_WIDTH,
    TEXT_COLOR
)



class Menu_Difficulty(Menu):

    def __init__(self, screen, screen_color):

        difficulty_text = Text("SELECT DIFFICULTY", 40, TEXT_COLOR, (SCREEN_WIDTH // 2, 80), FONT_TYPE)

        easy_button = Button((SCREEN_WIDTH // 2, 250), 180, 50, BUTTON_DEFAULT_COLOR, BUTTON_HOVER_COLOR, Text("EASY", 20, TEXT_COLOR, (0, 0), FONT_TYPE))
        normal_button =  Button((SCREEN_WIDTH // 2, 350), 180, 50, BUTTON_DEFAULT_COLOR, BUTTON_HOVER_COLOR, Text("NORMAL", 20, TEXT_COLOR, (0, 0), FONT_TYPE))
        hard_button = Button((SCREEN_WIDTH // 2, 450), 180, 50, BUTTON_DEFAULT_COLOR, BUTTON_HOVER_COLOR, Text("HARD", 20, TEXT_COLOR, (0, 0), FONT_TYPE))
        back_button = Button((SCREEN_WIDTH // 2, 600), 180, 50, BUTTON_DEFAULT_COLOR, BUTTON_HOVER_COLOR, Text("BACK", 20, TEXT_COLOR, (0, 0), FONT_TYPE))

        texts = [difficulty_text]
        buttons = [easy_button, normal_button, hard_button, back_button]

        super().__init__(screen, screen_color, texts, buttons)

        self.difficulty_selected = False
        self.easy_button = easy_button
        self.normal_button = normal_button
        self.hard_button = hard_button
        self.back_button = back_button

        self.active_enemies = []

    def handle(self, event_pos, all_entities, all_sprites):

        if self.back_button.is_clicked(event_pos):
            return "main_menu", self.active_enemies

        if self.difficulty_selected:
            return "game_start", self.active_enemies
        

        difficulty_map = {
            self.easy_button: (all_entities[1:2], all_entities[:2], "EASY"),
            self.normal_button: (all_entities[1:3], all_entities[:3], "NORMAL"),
            self.hard_button: (all_entities[1:], all_entities, "HARD")
        }

        for button, (active_enemies, adding_entities, label) in difficulty_map.items():

            if button.is_clicked(event_pos):

                self.active_enemies = active_enemies
                self.difficulty_selected = True
                all_sprites.add(*adding_entities)
                
                return "game_start", self.active_enemies
        
        return "select_difficulty", self.active_enemies
                        
            
        
    def reset_difficulty(self):
        self.difficulty_selected = False            