import pygame
from const import SIZE, PANEL_SIZE, SQUARE_SIZE, BACKGROUND, BOARD_LEN
from utils import get_move

def update_winning_panel(screen, font, player, arr):
    panel_time = pygame.Rect(SQUARE_SIZE * 20, PANEL_SIZE * 2.0, PANEL_SIZE, PANEL_SIZE * 1)
    pygame.draw.rect(screen, (200, 200, 200), panel_time, 0)
    print('arr : ', arr)
    output_string = "PLAYER: {0} HAS WON!".format(1 if player == 1 else 2)
    out_arr = "Winning: {0}".format(' '.join([','.join(map(str, x)) for x in arr]) if len(arr) else "10 Captures")
    text = font.render(output_string, True, (0,0,0))
    text2 = font.render(out_arr, True, (0,0,0))
    screen.blit(text, panel_time)
    screen.blit(text2, (SQUARE_SIZE * 20, 30))

    pygame.display.flip()

def is_winning_move(moves, pos, player):
    for i in range(0, 8, 2):
        ret = set()
        ret.add(pos)
        x, y = pos
        x, y = get_move(x, y, 1, i)
        while (x, y, player) in moves:
            x, y = get_move(x, y, 1, i)
            ret.add((x, y))
        
        x, y = pos
        x, y = get_move(x, y, 1, i + 1)
        while (x, y, player) in moves:
            x, y = get_move(x, y, 1, i + 1)
            ret.add((x, y))
        if len(ret) >= 5:
            return ret
    return []