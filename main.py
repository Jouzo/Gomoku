import pygame
from const import BOARD_SIZE, BOARD_LEN
from board import Board
from stone import get_ajusted_position
from game import do_minimax

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)


def main():
    pygame.display.init()
    pygame.font.init()
    screen = pygame.display.set_mode(BOARD_SIZE, 0, 32)

    board = Board(screen)

    running = True
    seconds = 0
    while running:
        pygame.time.wait(5)
        board.update_time(seconds)
        seconds += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                key = event.dict["key"]
                if key == 27:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if board.outline.collidepoint(pos):
                    x, y = get_ajusted_position(board.coordinates, pos)
                    if (x, y, 1) not in board.moves and (x, y, -1) not in board.moves:
                        do_minimax(board, x, y)
                        seconds = 0
    
    pygame.quit()

main()