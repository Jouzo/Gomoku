import pygame
import time
import textwrap
from const import SIZE, PANEL_SIZE, SQUARE_SIZE, BACKGROUND

class Board():
    def __init__(self, screen):
        self.background = pygame.image.load(BACKGROUND).convert()
        self.screen = screen
        self.outline = pygame.Rect(SQUARE_SIZE, SQUARE_SIZE, SIZE - SQUARE_SIZE * 2, SIZE - SQUARE_SIZE * 2)
        pygame.draw.rect(self.background, (0, 0, 0), self.outline, 3)
        self.outline.inflate_ip(20, 20)
        self.panel = pygame.Rect(SQUARE_SIZE * 20, 0, PANEL_SIZE, PANEL_SIZE * 1.5)
        self.font = pygame.font.SysFont("freemono.tff", 20)
        self.make()
        self.refresh_panel()

        pygame.display.update()
        
        self.available_moves = set()
        self.stones = { '1': 10, '-1': 10 }
        self.moves = []

    def refresh_panel(self):
        pygame.draw.rect(self.screen, (200, 200, 200), self.panel, 0)

    def update_time(self, frame_count):
        panel_time = pygame.Rect(SQUARE_SIZE * 20, PANEL_SIZE * 1.5, PANEL_SIZE, PANEL_SIZE * 1.5)
        pygame.draw.rect(self.screen, (200, 200, 200), panel_time, 0)
        total_seconds = frame_count // 60
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
        text = self.font.render(output_string, True, (0,0,0))
        self.screen.blit(text, panel_time)
        pygame.display.flip()

    def make(self):
        self.coordinates = []
        for i in range(18):
            self.coordinates.append(SQUARE_SIZE + SQUARE_SIZE * i)
            for j in range(18):
                x, y = SQUARE_SIZE + SQUARE_SIZE * j, SQUARE_SIZE + SQUARE_SIZE * i
                rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(self.background, (0, 0, 0), rect, 1)
        self.coordinates.append(SQUARE_SIZE + SQUARE_SIZE * 18)
        
        for i in range(3):
            for j in range(3):
                coords = (SQUARE_SIZE + ((SIZE - SQUARE_SIZE * 2) // 6) + (((SIZE - SQUARE_SIZE * 2) // 3) * i), SQUARE_SIZE + ((SIZE - SQUARE_SIZE * 2) // 6) + (((SIZE - SQUARE_SIZE * 2) // 3) * j))
                pygame.draw.circle(self.background, (0, 0, 0), coords, SIZE // 110, 0)
        
        self.screen.blit(self.background, (0, 0))