import pygame
from const import SIZE, PANEL_SIZE, BOARD_SIZE, SQUARE_SIZE
from board import Board
from stone import get_ajusted_position, put_stone
from minimax import minimax

def main():
    pygame.display.init()
    pygame.font.init()
    screen = pygame.display.set_mode(BOARD_SIZE, 0, 32)

    board = Board(screen)
    coordinates = board.coordinates
    matrice = [[0 for _ in range(19)] for _ in range(19)]

    p = 1
    running = True

    seconds = 0
    while running:
        pygame.time.wait(5)
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
                    x, y = get_ajusted_position(coordinates, pos)
                    print(x, y)
                    if not matrice[y][x]:
                        put_stone(p, screen, (coordinates[x], coordinates[y]))
                        matrice[y][x] = p + 1
                        _hash = minimax(matrice)
                        board.update_panel(_hash)
                        p ^= 1
                        seconds = 0
                    print(matrice)
        
        seconds += 1
        board.update_time(seconds)
    
    pygame.quit()

main()