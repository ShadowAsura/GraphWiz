import pygame
from .buttons import Button

class SidePanel:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (200, 200, 200)  # Light gray
        self.buttons = []
        self.add_algorithm_buttons()

    def add_algorithm_buttons(self):
        btn_width = self.width - 20  # Padding of 10 on each side
        btn_height = 30
        algorithms = ["BFS", "DFS", "Dijkstra"]
        for index, algo in enumerate(algorithms):
            btn_x = self.x + 10  # Padding of 10
            btn_y = self.y + (index * (btn_height + 10)) + 10  # Padding and spacing of 10
            self.buttons.append(Button(btn_x, btn_y, btn_width, btn_height, algo, (0, 150, 0), (255, 255, 255)))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        for button in self.buttons:
            button.draw(screen)

    def is_clicked(self, x, y):
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height
