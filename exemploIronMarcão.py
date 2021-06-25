import pygame
import random
import time
pygame.init()  # função para iniciar o pygame
explosaoSound = pygame.mixer.Sound("assets/explosao.wav")
missilSound = pygame.mixer.Sound("assets/missile.wav")
icone = pygame.image.load("assets/ironIcon.png")
pygame.display.set_caption("Iron Man do Marcão")
pygame.display.set_icon(icone)
largura = 800
altura = 600
display = pygame.display.set_mode((largura, altura))
fps = pygame.time.Clock()
fundo = pygame.image.load("assets/sky.png")
iron = pygame.image.load("assets/ironLarge.png")
missel = pygame.image.load("assets/missile.png")
# [ini] cores em RGB (https://www.rapidtables.com/web/color/RGB_Color.html)
preto = (0, 0, 0)
branco = (255, 255, 255)
# [fim] cores
def text_objects(texto, fonte):
    textSurface = fonte.render(texto, True, preto)
    return textSurface, textSurface.get_rect()
def message_display(text):
    fonte = pygame.font.Font("freesansbold.ttf",50)
    TextSurf, TextRect = text_objects(text, fonte)
    TextRect.center = ((largura/2), (altura/2))
    display.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    jogo()
def dead(desvios):
    pygame.mixer.Sound.play(explosaoSound)
    pygame.mixer.music.stop()
    message_display("Você Morreu com "+str(desvios)+" desvios")

def escrevendoPlacar(desvios):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("Desvios:"+str(desvios), True, branco)
    display.blit(texto, (0, 0))
    
def jogo():
    pygame.mixer.music.load('assets/ironsound.mp3')
    pygame.mixer.music.play(-1) # -1 é loopig infinito
    ironPosicaoX = largura * 0.45
    ironPosicaoY = altura * 0.8
    ironLargura = 120
    movimentoX = 0
    missilPosicaoX = largura * 0.45
    missilPosicaoY = -220
    missilLargura = 50
    missilAltura = 250
    missilVelocidade = 5

    desvios = 0

    while True:
        # [ini] bloco de comando para verificar interação do usuário:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()  # break para executar o fim do código
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimentoX = -10
                elif evento.key == pygame.K_RIGHT:
                    movimentoX = 10
            if evento.type == pygame.KEYUP:
                movimentoX = 0

        # [fim] bloco de comando para verificar interação do usuário:
        display.fill(branco)  # função para mudar a cor de fundo da tela
        display.blit(fundo, (0, 0))  # inserir imagem da tela
        ironPosicaoX = ironPosicaoX + movimentoX
        if ironPosicaoX < 0:
            ironPosicaoX = 0
        elif ironPosicaoX > 680:
            ironPosicaoX = 680
        # inserir imagem da tela
        display.blit(iron, (ironPosicaoX, ironPosicaoY))
        display.blit(missel, (missilPosicaoX, missilPosicaoY))
        missilPosicaoY = missilPosicaoY + missilVelocidade
        # [ini] quando ele ultrapassa a barreira (fundo), começa em um lugar novo
        if missilPosicaoY > altura:
            pygame.mixer.Sound.play(missilSound)
            missilPosicaoY = -220
            missilVelocidade += 1
            missilPosicaoX = random.randrange(0, largura-50)
            desvios = desvios + 1
        # [fim] quando ele ultrapassa a barreira (fundo), começa em um lugar novo
        escrevendoPlacar(desvios)
        # [ini]análise de colisão:
        if ironPosicaoY < missilPosicaoY + missilAltura:
            if ironPosicaoX < missilPosicaoX and ironPosicaoX+ironLargura > missilPosicaoX or missilPosicaoX+missilLargura > ironPosicaoX and missilPosicaoX+missilLargura < ironPosicaoX+ironLargura:
                dead(desvios)
        # [fim]análise de colisão:
        pygame.display.update()
        fps.tick(60)
jogo()
print("Volte sempre....")
