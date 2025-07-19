import pygame
from ui import Text
from constants import (
    TEXT_COLOR,
    FONT_TYPE,
    SCREEN_WIDTH
)


class Survival_Timer:

    def __init__(self, screen):
        
        self.screen = screen
        self.time_text = Text("SURVIVED:", 20, TEXT_COLOR, (SCREEN_WIDTH // 2, 200), FONT_TYPE)
        
        self.my_time = 0

        self.elapsed_time = 0
        self.active = False
        self.starting_time = 0

    
    def start_timer(self):
        if not self.active:
            self.starting_time = pygame.time.get_ticks()
            self.active = True
        
        self.draw_timer()


    def pause_timer(self):

        if self.active:
            current_time = pygame.time.get_ticks()
            self.elapsed_time += current_time - self.starting_time
            self.active = False
        
        self.draw_timer()

    

    def reset_timer(self):
        self.elapsed_time = 0
        self.active = False
        self.starting_time = 0
    



    def draw_timer(self):

        self.time_text.update_text(f"SURVIVED: {self.get_current_timer() // 1000}s")
        self.time_text.draw(self.screen)


    def get_current_timer(self):

        if self.active:
            current_time = pygame.time.get_ticks()
            return self.elapsed_time + (current_time - self.starting_time)
        else:
            return self.elapsed_time


    
