import pygame
import time
from const import BOARD_LEN
from random import choice
from winning import is_winning_move, update_winning_panel
from move import get_available_move
from stone import put_stone
from minimax import minimax, sort_moves
from rules import capture
from state import State

def play_move(board, player, x, y):
    put_stone(player, board, (board.coordinates[x], board.coordinates[y]))
    win = is_winning_move(board.moves, (x, y), player)
    if len(win) or board.captures[str(player)] >= 10:
        update_winning_panel(board.screen, board.font, player, win)
        # time.sleep(3)
        while True:
            pass
        pygame.quit()
        exit(0)
    pygame.display.update(board.outline)
    board.moves.add((x, y, player))

def remove_move(board, captures):
    board.make()
    for x, y, p in captures:
        board.moves.remove((x, y, p))
        board.available_moves.add((x, y))
        if board.captures[str(-p)] < 10:
            board.captures[str(-p)] += 1
    for x, y, p in board.moves:
        put_stone(p, board, (board.coordinates[x], board.coordinates[y]))
    pygame.display.update(board.outline)


def play(board, x, y, player):
    c = capture(board.moves, x, y, player)
    if len(c):
        remove_move(board, c)
    
    play_move(board, player, x, y)
    board.available_moves.discard((x, y))
    board.available_moves.update(get_available_move(board.moves, x, y))
    return True

def do_minimax(board, x, y):
    if play(board, x, y, 1):
        board.available_moves.update(get_available_move(board.moves, x, y))
        # m = sort_moves(board, -1, 4)
        board.player = -1
        _, (x, y) = minimax(board, 3, -1, float('-Inf'), float('Inf'))
        play(board, x, y, -1)
        # print('yo : ', yo)
        # play(board, *m[0], -1)
    else:
        board.wrong_move()
