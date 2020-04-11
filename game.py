import pygame
import time
from random import choice
from winning import is_winning_move, update_winning_panel
from utils import get_available_move
from stone import put_stone
from minimax import minimax, get_total_score

def play_move(board, p, x, y):
    put_stone(p, board, (board.coordinates[x], board.coordinates[y]))
    if is_winning_move(board.matrice, (x, y), p):
        update_winning_panel(board.screen, board.font, p)
        time.sleep(3)
        pygame.quit()
        exit(0)
    board.matrice[y][x] = p


def do_minimax(board, x, y):
    board.available_moves.discard((x, y))
    p = 1
    play_move(board, p, x, y)

    board.available_moves.update(get_available_move(board.matrice))
    # print('matrice before : ',  board.matrice)
    _, (x, y) = minimax(board, board.matrice, 3, True, float('-Inf'), float('Inf'))
    # print('matrice after:   ',  board.matrice)
    board.available_moves.discard((x, y))
    p = 2
    play_move(board, p, x, y)