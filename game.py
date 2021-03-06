import pygame
import time
from random import choice
from winning import is_winning_move, update_winning_panel
from move import get_available_move
from stone import put_stone
from minimax import minimax, get_total_score
from rules import capture, self_capture

def play_move(board, player, x, y):
    put_stone(player, board, (board.coordinates[x], board.coordinates[y]))
    if is_winning_move(board.matrice, (x, y), player) or board.stones[str(-player)] <= 0:
        update_winning_panel(board.screen, board.font, player)
        time.sleep(3)
        pygame.quit()
        exit(0)
    board.matrice[y][x] = player
    board.moves.append((x, y, player))
    pygame.display.update(board.outline)

def remove_move(board, captures):
    board.make()
    for x, y, p in captures:
        board.moves.remove((x, y, p))
        board.matrice[y][x] = 0
        board.stones[str(p)] -= 1
    for x, y, p in board.moves:
        put_stone(p, board, (board.coordinates[x], board.coordinates[y]))
    pygame.display.update(board.outline)

def check_move(board, x, y, player):
    if self_capture(board.matrice, x, y, player):
        return False
    else:
        return True

def play(board, x, y, player):
    if check_move(board, x, y, player):
        c = capture(board.matrice, x, y, player)
        if len(c):
            remove_move(board, c)
        
        play_move(board, player, x, y)
        board.available_moves.discard((x, y))
        return True
    else:
        return False


def do_minimax(board, x, y):
    if play(board, x, y, 1):
        board.available_moves.update(get_available_move(board.matrice))
        _, (x, y) = minimax(board, board.matrice, 3, -1, float('-Inf'), float('Inf'))
        play(board, x, y, -1)
    else:
        board.wrong_move()
