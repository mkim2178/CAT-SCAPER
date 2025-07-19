import pygame

class Button:

    def __init__(self, center_pos, width, height, default_color, hover_color, text):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = center_pos
        self.default_color = default_color
        self.hover_color = hover_color
        self.current_color = default_color
        self.text = text

        if self.text:
            self.text.set_center(self.rect.center)

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
    
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
    def update_color(self):
        self.current_color = self.hover_color if self.is_hovered() else self.default_color
    
    def update_text(self, new_text):
        self.text.update_text(new_text)

    def draw(self, screen):

        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=10)
        if self.text:
            self.text.draw(screen)