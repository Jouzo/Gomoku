import pygame

SIZE = 820
SQUARE_SIZE = SIZE // 20
HALF_SQUARE = SQUARE_SIZE // 2
BOARD_SIZE = (SIZE, SIZE)
STONE_SIZE = SIZE // 23
BACKGROUND = 'img/goban.jpg'
STONES = ["img/white_stone.png", "img/black_stone.png"]

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
    stone = pygame.image.load(STONES[player]).convert_alpha()
    picture = pygame.transform.scale(stone, (STONE_SIZE, STONE_SIZE))
    pos = (pos[0] - STONE_SIZE // 2, pos[1] - STONE_SIZE // 2)
    screen.blit(picture, pos)

class Board():
    def __init__(self, screen):
        self.background = pygame.image.load(BACKGROUND).convert()
        self.screen = screen
        self.outline = pygame.Rect(SQUARE_SIZE, SQUARE_SIZE, SIZE - SQUARE_SIZE * 2, SIZE - SQUARE_SIZE * 2)
        pygame.draw.rect(self.background, (0, 0, 0), self.outline, 3)
        self.outline.inflate_ip(20, 20)
        self.coordinates = []
        self.make()

    def make(self):
        for i in range(18):
            self.coordinates.append(SQUARE_SIZE + SQUARE_SIZE * i)
            for j in range(18):
                x, y = SQUARE_SIZE + SQUARE_SIZE * j, SQUARE_SIZE + SQUARE_SIZE * i
                rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(self.background, (0, 0, 0), rect, 1)
        self.coordinates.append(SQUARE_SIZE + SQUARE_SIZE * 18)
        
        for i in range(3):
            for j in range(3):
                coords = (SQUARE_SIZE + ((SIZE - SQUARE_SIZE * 2) // 6) + (((SIZE - SQUARE_SIZE * 2) // 3) * i), SQUARE_SIZE + ((SIZE - SQUARE_SIZE * 2) // 6) + (((SIZE - SQUARE_SIZE * 2) // 3) * j))
                pygame.draw.circle(self.background, (0, 0, 0), coords, SIZE // 110, 0)
            
        self.screen.blit(self.background, (0, 0))
        pygame.display.update()