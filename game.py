import pygame
import time
from random import choice
from winning import is_winning_move, update_winning_panel
from utils import get_available_move
from stone import put_stone
from minimax import minimax, get_total_score

def play_move(board, p, x, y):
    put_stone(p, board.screen, (board.coordinates[x], board.coordinates[y]))
    if is_winning_move(board.matrice, (x, y), p):
        update_winning_panel(board.screen, board.font, p)
        time.sleep(3)
        pygame.quit()
        exit(0)
    board.matrice[y][x] = p


def do_minimax(board, x, y):
    p = 1
    board.available_moves.discard((x, y))
    play_move(board, p, x, y)
    score = get_total_score(board.matrice)
    # print('score : ', score)
    board.available_moves.update(get_available_move(board.matrice))
    # print(board.available_moves)
    p = 2
    # x, y = get_rand_xy(board.available_moves)
    print("--- NEW MINIMAX ---")
    # print('board.matrice before : ', board.matrice)
    yo, (x, y) = minimax(board, board.matrice, 3, True)
    # print('board.matrice after : ', board.matrice)
    print('YO : ', yo)
    print(x, y)
    board.available_moves.discard((x, y))
    play_move(board, p, x, y)
    score = get_total_score(board.matrice)
    print('score : ', score)
    # print(available_moves)