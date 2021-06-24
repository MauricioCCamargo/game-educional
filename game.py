import pygame
import random
import time
import os
from funcoes import colisaoparede
pygame.init()
fundo = pygame.image.load("assets/fundo.png")
largura = 1026
altura = 728
display = pygame.display.set_mode((largura, altura))
fps = pygame.time.Clock()
lixovermelho = pygame.image.load("assets/lixovermelho.png")
lixoazul = pygame.image.load("assets/lixoazul.png")
lixoamarelo = pygame.image.load("assets/lixoamarelo.png")
lixoverde = pygame.image.load("assets/lixoverde.png")
papel = pygame.image.load("assets/papel.png") 

movimentoX = 0
lixoPosiçãoX = largura * 0.45
lixoPosiçãoY = 0 

LarguraPapel = 49
alturaPapel = 44
while True:
    display.blit(fundo,(0,0))
    display.blit(lixoamarelo,(100,600))
    display.blit(lixoverde,(300,600))
    display.blit(lixovermelho,(600,600))
    display.blit(lixoazul,(850,600))
    fps.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                movimentoX = -5
            elif evento.key == pygame.K_RIGHT:
                movimentoX = +5
        if evento.type == pygame.KEYUP:
            movimentoX = 0         
    colisaoParede(LarguraPapel,lixoPosiçãoX)

    
    
    
    
    display.blit(papel,(lixoPosiçãoX,lixoPosiçãoY))
    
    lixoPosiçãoX = lixoPosiçãoX + movimentoX 
        
        
        
        
    pygame.display.update()