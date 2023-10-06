import pygame

class Button:
    def __init__(self, x, y, width, height, text, color, font_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.font_color = font_color

    def draw(self, screen):
        import pygame
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont(None, 24)
        label = font.render(self.text, 1, self.font_color)
        screen.blit(label, (self.x + (self.width // 2 - label.get_width() // 2), self.y + (self.height // 2 - label.get_height() // 2)))

    def is_clicked(self, x, y):
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height
