import pygame
import os
import random
from funcoes import colisaoparede
import time
pygame.init()
fundo = pygame.image.load("assets/fundo.png")
largura = 1026
altura = 728
display = pygame.display.set_mode((largura, altura))
display.blit(fundo,(0,0))
fps = pygame.time.Clock()
lixovermelho = pygame.image.load("assets/Vermelho_.png")
lixoazul = pygame.image.load("assets/Azul_.png")
lixoamarelo = pygame.image.load("assets/Amarelo_.png")
lixoverde = pygame.image.load("assets/Verde_.png")
papel = pygame.image.load("assets/Paupel.png") 
plastico = pygame.image.load("assets/plastico.png")
metal = pygame.image.load("assets/metal.png")
vidro = pygame.image.load("assets/vidro.png")

lixos = [papel,vidro,plastico,metal]
cor1 = (102,255,255)
def text_objects(texto, fonte):
    textSurface = fonte.render(texto, True, cor1)
    return textSurface, textSurface.get_rect()
def message_display(text):
    fonte = pygame.font.Font("freesansbold.ttf",30)
    TextSurf, TextRect = text_objects(text, fonte)
    TextRect.center = ((largura/2), (altura/2))
    display.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
message_display("voce devera acertar os residuos sólidos em seus devidos lugares")
display.blit(fundo,(0,0))
message_display("mova-os para os lados utilizando as setas")
#texto1 = letras.render("voce devera acertar os residuos sólidos em seus devidos lugares",True,cor1)

#texto2 = letras.render("mova-os para os lados utilizando as setas",True,cor1)

def escrevendoPlacar(acertos):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("Acertos:"+str(acertos), True, cor1)
    display.blit(texto, (0, 0))
def jogo():
    movimentoX = 0
    lixoPosicaoX = largura * 0.45
    lixoPosicaoY = 0 
    lixoVelocidade = 3
    LarguraPapel = 114
    alturaPapel = 109
    azulposicaoX = 750
    azulposicaoY = 500
    amareloposicaoX = 50
    amareloposicaoY = 500
    verdeposicaoX = 300
    verdeposicaoY = 500
    vermelhoposicaoX = 530
    vermelhoposicaoY = 500
    larguraverde = 175
    alturaverde = 106
    larguravermelho = 178
    alturavermelho = 106
    larguraazul = 181
    alturaazul =108
    larguraamarelo = 175
    alturaamarelo = 105
    larguraPlastico = 100
    alturaPlastico = 208
    larguraMetal  = 100
    alturaMetal = 174
    larguraVidro = 77
    alturaVidro = 149
    acertos = 0
    pygame.mixer.music.load('assets/musica.wav')
    pygame.mixer.music.play(-1)
    lixoescolhido = random.choice(lixos)
    while True:
        
        
        escrevendoPlacar(acertos)
        display.blit(fundo,(0,0))
        display.blit(lixoamarelo,(amareloposicaoX,amareloposicaoY ))
        display.blit(lixoverde,(verdeposicaoX,verdeposicaoY ))
        display.blit(lixovermelho,(vermelhoposicaoX,vermelhoposicaoY))
        display.blit(lixoazul,(azulposicaoX,azulposicaoY))
        
        
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
    
        
        display.blit(lixoescolhido,(lixoPosicaoX,lixoPosicaoY))
        lixoPosicaoY = lixoPosicaoY + lixoVelocidade
        lixoPosicaoX = lixoPosicaoX + movimentoX 
        if lixoPosicaoX < 0:
            lixoPosicaoX = 0
        if lixoPosicaoX > 1026 - LarguraPapel:
            lixoPosicaoX = 1026 - LarguraPapel
        if lixoPosicaoY  > 728 - alturaPapel:
            lixoPosicaoY = 0 
            lixoescolhido = random.choice(lixos)
            message_display("você deve acertar a lixeira correta")
            time.sleep(2)
        if lixoescolhido == plastico:
            if lixoPosicaoY + alturaPlastico >= vermelhoposicaoY and lixoPosicaoX >= vermelhoposicaoX and lixoPosicaoX <= vermelhoposicaoX + larguravermelho: 
                message_display("você acertou")
                time.sleep(2)
                lixoPosicaoX = largura * 0.45
                lixoPosicaoY = 0
                lixoescolhido = random.choice(lixos)
                acertos =+ 1
        if lixoescolhido == metal:
            if lixoPosicaoY + alturaMetal >= amareloposicaoY and lixoPosicaoX >= amareloposicaoX and lixoPosicaoX <= amareloposicaoX + larguraamarelo: 
                message_display("você acertou")
                time.sleep(2)
                lixoPosicaoX = largura * 0.45
                lixoPosicaoY = 0
                lixoescolhido = random.choice(lixos)
                acertos=+ 1
        if lixoescolhido == vidro:
            if lixoPosicaoY + alturaVidro >= verdeposicaoY and lixoPosicaoX >= verdeposicaoX and lixoPosicaoX <= verdeposicaoX + larguraverde: 
                message_display("você acertou")
                time.sleep(2)
                lixoPosicaoX = largura * 0.45
                lixoPosicaoY = 0
                lixoescolhido = random.choice(lixos)
                acertos=+ 1
        if lixoescolhido == papel:
            if lixoPosicaoY + alturaPapel >= azulposicaoY and lixoPosicaoX >= azulposicaoX and lixoPosicaoX <= azulposicaoX + larguraazul: 
                message_display("você acertou")
                time.sleep(2)
                lixoPosicaoX = largura * 0.45
                lixoPosicaoY = 0
                lixoescolhido = random.choice(lixos)
                acertos =+ 1
        pygame.display.update()
        fps.tick(60)
jogo()     

        
    