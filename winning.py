import pygame
from const import SIZE, PANEL_SIZE, SQUARE_SIZE, BACKGROUND
from utils import get_move

def update_winning_panel(screen, font, p):
    panel_time = pygame.Rect(SQUARE_SIZE * 20, PANEL_SIZE * 2.0, PANEL_SIZE, PANEL_SIZE * 1)
    pygame.draw.rect(screen, (200, 200, 200), panel_time, 0)
    output_string = "PLAYER: {0} HAS WON !".format(p)
    text = font.render(output_string, True, (0,0,0))
    screen.blit(text, panel_time)
    pygame.display.flip()

def is_winning_move(matrice, pos, player):
    _len = len(matrice)
    X, Y = pos
    for i in range(8):
        count = 0
        for j in range(1, 5):
            x, y = get_move(X, Y, j, i)
            if 0 <= x < _len and 0 <= y < _len:
                if matrice[y][x] == player:
                    count += 1
        if count >= 4:
            return 1
    return 0