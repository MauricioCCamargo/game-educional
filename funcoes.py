
def colisaoparede(largura,altura,lixoposiçãoY,lixoPosiçãoX):
    if lixoPosiçãoX < 0:
            lixoPosçãoX = 0
    if lixoPosiçãoX > 1026 - largura:
            lixoPosiçãoX = 1026 - largura
    if lixoposiçãoY  > 728 - altura:
            lixoposicaoY = 0 
            