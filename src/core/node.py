import pygame

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 0, 0)  # RED
        self.radius = 10

    def draw(self, screen):
        import pygame.gfxdraw
        pygame.gfxdraw.aacircle(screen, self.x, self.y, self.radius, self.color)
        pygame.gfxdraw.filled_circle(screen, self.x, self.y, self.radius, self.color)


    def is_clicked(self, x, y):
        return (self.x - x) ** 2 + (self.y - y) ** 2 <= self.radius ** 2

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)