import pygame
from board import Board, get_ajusted_position, put_stone

SIZE = 820
BOARD_SIZE = (SIZE, SIZE)

def main():
    pygame.display.init()
    screen = pygame.display.set_mode(BOARD_SIZE, 0, 32)

    board = Board(screen)
    coordinates = board.coordinates

    p = 1
    running = True

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
                    put_stone(p, screen, (coordinates[x], coordinates[y]))
                    p ^= 1

        pygame.display.flip()

    pygame.quit()

main()