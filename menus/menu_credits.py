from menus.menu import Menu
from ui import Button, Text
from constants import (
    BUTTON_DEFAULT_COLOR,
    BUTTON_HOVER_COLOR,
    FONT_TYPE,
    SCREEN_WIDTH,
    TEXT_COLOR
)


class Menu_Credits(Menu):

    def __init__(self, screen, screen_color):

        credits_text = Text("CREDITS", 40, TEXT_COLOR, (SCREEN_WIDTH // 2, 80), FONT_TYPE)


        sprites_credit_text = Text("Sprites: Cat & Mouse by pebonius (OpenGameArt)", 13, TEXT_COLOR, (SCREEN_WIDTH // 2, 150), FONT_TYPE)

        background_music_credit_text = Text("Music: \"Game Gaming Minecraft Background Music\" by Ievgen Poltavskyi (Pixabay)", 11, TEXT_COLOR, (SCREEN_WIDTH // 2, 180), FONT_TYPE)

        sound_effect_credit_text = Text("Sound Effects: 8 bit menu highlight by Fupi (OpenGameArt), bomb_explosion_8bit by Luke.RUSTLTD (OpenGameArt)", 11, TEXT_COLOR, (SCREEN_WIDTH // 2, 210), FONT_TYPE)

        font_credit_text = Text("Font: \"Press Start 2P\" by Cody P. (SIL Open Font License). See fonts/OFL.txt for full license.", 11, TEXT_COLOR, (SCREEN_WIDTH // 2, 240), FONT_TYPE)

        back_button = Button((SCREEN_WIDTH // 2, 300), 180, 50, BUTTON_DEFAULT_COLOR, BUTTON_HOVER_COLOR, Text("BACK", 20, TEXT_COLOR, (0, 0), FONT_TYPE))



        texts = [credits_text, sprites_credit_text, background_music_credit_text, sound_effect_credit_text, font_credit_text]
        buttons = [back_button]

        super().__init__(screen, screen_color, texts, buttons)

        self.back_button = back_button


    def handle(self, event_pos):
        if self.back_button.is_clicked(event_pos):

            return "main_menu"

        return "credits"

