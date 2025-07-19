from menus.menu import Menu
from ui import Button, Text
from constants import (
    BUTTON_DEFAULT_COLOR,
    BUTTON_HOVER_COLOR,
    FONT_TYPE,
    SCREEN_WIDTH,
    TEXT_COLOR
)


class Menu_Settings(Menu):

    def __init__(self, screen, screen_color):

        settings_text = Text("SETTINGS", 40, TEXT_COLOR, (SCREEN_WIDTH // 2, 80), FONT_TYPE)
        bgm_text = Text("BGM:", 40, TEXT_COLOR, (SCREEN_WIDTH // 2 - 180, 300), FONT_TYPE)
        sfx_text = Text("SFX:", 40, TEXT_COLOR, (SCREEN_WIDTH // 2 - 180, 400), FONT_TYPE)

        bgm_on_off_button = Button((SCREEN_WIDTH // 2, 300), 180, 50, BUTTON_DEFAULT_COLOR, BUTTON_HOVER_COLOR, Text("ON", 20, TEXT_COLOR, (0, 0), FONT_TYPE))
        sfx_on_off_button = Button((SCREEN_WIDTH // 2, 400), 180, 50, BUTTON_DEFAULT_COLOR, BUTTON_HOVER_COLOR, Text("ON", 20, TEXT_COLOR, (0, 0), FONT_TYPE))
        back_button = Button((SCREEN_WIDTH // 2, 500), 180, 50, BUTTON_DEFAULT_COLOR, BUTTON_HOVER_COLOR, Text("BACK", 20, TEXT_COLOR, (0, 0), FONT_TYPE))

        texts = [settings_text, bgm_text, sfx_text]
        buttons = [bgm_on_off_button, sfx_on_off_button, back_button]

        super().__init__(screen, screen_color, texts, buttons)

        self.bgm_on_off_button = bgm_on_off_button
        self.bgm_on = True

        self.sfx_on_off_button = sfx_on_off_button
        self.sfx_on = True

        self.back_button = back_button


    def handle(self, event_pos, bgm, sfx_sounds):

        if self.back_button.is_clicked(event_pos):
            return "main_menu"
        
        
        if self.bgm_on_off_button.is_clicked(event_pos):

            self.bgm_on = not self.bgm_on
            bgm.set_volume(0.1 if self.bgm_on else 0.0)
            self.bgm_on_off_button.update_text("ON" if self.bgm_on else "OFF")


        if self.sfx_on_off_button.is_clicked(event_pos):

            self.sfx_on = not self.sfx_on
            for sfx in sfx_sounds:
                sfx.set_volume(0.2 if self.sfx_on else 0.0)
            self.sfx_on_off_button.update_text("ON" if self.sfx_on else "OFF")

        return "settings"