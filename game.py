import pygame
import time
from random import choice
from winning import is_winning_move, update_winning_panel
from move import get_available_move
from stone import put_stone
from minimax import minimax, get_total_score
from rules import capture

def play_move(board, p, x, y):
    put_stone(p, board, (board.coordinates[x], board.coordinates[y]))
    if is_winning_move(board.matrice, (x, y), p):
        update_winning_panel(board.screen, board.font, p)
        time.sleep(3)
        pygame.quit()
        exit(0)
    board.matrice[y][x] = p
    board.moves.append((x, y, p))
    pygame.display.update(board.outline)

def remove_move(board, captures):
    board.make()
    for x, y, p in captures:
        board.moves.remove((x, y, p))
        board.matrice[y][x] = 0
    for x, y, p in board.moves:
        put_stone(p, board, (board.coordinates[x], board.coordinates[y]))
    pygame.display.update(board.outline)

def play(board, x, y, p):
    play_move(board, p, x, y)
    board.available_moves.discard((x, y))

    c = capture(board.matrice, p, x, y)
    if len(c):
        remove_move(board, c)

def do_minimax(board, x, y):
    play(board, x, y, 1)
    board.available_moves.update(get_available_move(board.matrice))
    _, (x, y) = minimax(board, board.matrice, 3, True, float('-Inf'), float('Inf'))
    play(board, x, y, 2)