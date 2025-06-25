import pygame

class Screen:

    def __init__(self, screen, screen_color, texts=None, buttons=None):

        self.screen = screen
        self.screen_color = screen_color
        self.texts = texts if texts else []
        self.buttons = buttons if buttons else []
    

    def fill(self):

        self.screen.fill(self.screen_color)

        if self.texts:
            for text in self.texts:
                text.draw(self.screen)

        if self.buttons:
            for button in self.buttons:
                button.update_color()
                button.draw(self.screen)
    