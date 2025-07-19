import pygame

class Text:

    def __init__(self, text, font_size, font_color, font_center_pos, font_type=None):
        self.text = text
        self.font = pygame.font.Font(font_type, font_size)
        self.font_color = font_color
        self.surface = self.font.render(text, True, self.font_color)
        self.rect = self.surface.get_rect(center=font_center_pos)
    
    def draw(self, target_surface):
        target_surface.blit(self.surface, self.rect)

    def update_text(self, new_text):
        self.text = new_text
        self.surface = self.font.render(new_text, True, self.font_color)
        self.rect = self.surface.get_rect(center=self.rect.center)

    def set_center(self, center_pos):
        self.rect = self.surface.get_rect(center=center_pos)
    
    def get_position(self):
        print(self.rect.left, self.rect.top, self.rect.right, self.rect.bottom)
