import pygame
import time
import textwrap
from const import SIZE, PANEL_SIZE, SQUARE_SIZE, BACKGROUND, BOARD_SIZE, BOARD_LEN

class Board():
    def __init__(self, screen):
        self.background = pygame.image.load(BACKGROUND).convert()
        self.screen = screen
        self.outline = pygame.Rect(SQUARE_SIZE, SQUARE_SIZE, SIZE - SQUARE_SIZE * 2, SIZE - SQUARE_SIZE * 2)
        pygame.draw.rect(self.background, (0, 0, 0), self.outline, 3)
        self.outline.inflate_ip(20, 20)
        self.panel = pygame.Rect(SQUARE_SIZE * BOARD_LEN + 1, 0, PANEL_SIZE, PANEL_SIZE * 1.5)
        self.font = pygame.font.SysFont("freemono.tff", 20)
        self.make()
        self.refresh_panel()

        pygame.display.update()
        
        self.available_moves = set()
        self.captures = { '1': 0, '-1': 0 }
        self.moves = set()

    def refresh_panel(self):
        pygame.draw.rect(self.screen, (200, 200, 200), self.panel, 0)

    def wrong_move(self):
        panel_time = pygame.Rect(SQUARE_SIZE * BOARD_LEN + 1, PANEL_SIZE, PANEL_SIZE, PANEL_SIZE * 1.5)
        pygame.draw.rect(self.screen, (200, 200, 200), panel_time, 0)
        output_string = "Illegal move !"
        text = self.font.render(output_string, True, (0,0,0))
        self.screen.blit(text, panel_time)
        pygame.display.flip()

    def update_time(self, frame_count):
        panel_time = pygame.Rect(SQUARE_SIZE * BOARD_LEN + 1, PANEL_SIZE * 1.5, PANEL_SIZE, PANEL_SIZE * 1.5)
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
        for i in range(BOARD_LEN - 1):
            self.coordinates.append(SQUARE_SIZE + SQUARE_SIZE * i)
            for j in range(BOARD_LEN - 1):
                x, y = SQUARE_SIZE + SQUARE_SIZE * j, SQUARE_SIZE + SQUARE_SIZE * i
                rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(self.background, (0, 0, 0), rect, 1)
        self.coordinates.append(SQUARE_SIZE + SQUARE_SIZE * BOARD_LEN - 1)
        
        for i in range(3):
            for j in range(3):
                coords = (SQUARE_SIZE + ((SIZE - SQUARE_SIZE * 2) // 6) + (((SIZE - SQUARE_SIZE * 2) // 3) * i), SQUARE_SIZE + ((SIZE - SQUARE_SIZE * 2) // 6) + (((SIZE - SQUARE_SIZE * 2) // 3) * j))
                pygame.draw.circle(self.background, (0, 0, 0), coords, SIZE // 110, 0)
        
        self.screen.blit(self.background, (0, 0))