import pygame
import random
import time
pygame.init()
fundo = pygame.image.load("assets/fundo.png")
largura = 1026
altura = 728
display = pygame.display.set_mode((largura, altura))
fps = pygame.time.Clock()
lixos = pygame.image.load("assets/lixos.png")
