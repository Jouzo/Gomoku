import pygame
from const import HALF_SQUARE, STONES, STONE_SIZE

def get_ajusted_position(coordinates, pos):
    x, y = 0, 0
    pos = (pos[0] - HALF_SQUARE, pos[1] - HALF_SQUARE)
    if pos[0] > coordinates[17]:
        x = 18
    if pos[1] > coordinates[17]:
        y = 18
    for i in range(len(coordinates)):
        if pos[0] < coordinates[i] and (not i or pos[0] >= coordinates[i - 1]) and not x:
            x = i
        if pos[1] <= coordinates[i] and (not i or pos[1] >= coordinates[i - 1]) and not y:
            y = i
    return (x, y)

def put_stone(player, screen, pos):
    stone = pygame.image.load(STONES[player - 1]).convert_alpha()
    picture = pygame.transform.scale(stone, (STONE_SIZE, STONE_SIZE))
    pos = (pos[0] - STONE_SIZE // 2, pos[1] - STONE_SIZE // 2)
    screen.blit(picture, pos)