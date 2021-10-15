import pygame

WIDTH, HEIGHT = 640, 640
ROWS, COLS = 8,8
SQUARE_SIZE = WIDTH//COLS

# rgb colors
RED = (255,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (128,128,128)

CROWN = pygame.transform.scale(pygame.image.load('assests/crown.png'), (30, 20))
