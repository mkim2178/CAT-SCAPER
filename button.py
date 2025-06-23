import pygame

class Button:

    def __init__(self, center_pos, width, height, default_color, text=None, hover_color=None):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = center_pos
        self.default_color = default_color
        self.hover_color = hover_color or default_color
        self.current_color = default_color
        self.text = text

        if self.text:
            self.text.set_center(self.rect.center)

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
    
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
    def draw(self, screen):

        if self.is_hovered():
            self.current_color = self.hover_color
        else:
            self.current_color = self.default_color

        pygame.draw.rect(screen, self.current_color, self.rect)
        if self.text:
            self.text.draw(screen)