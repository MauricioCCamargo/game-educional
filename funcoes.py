import os
def colisaoParede(larguraObj,lixoPosiçãoX):
    if lixoPosiçãoX < 0:
        lixoPosiçãoX = 0
    if lixoPosiçãoX > 1026 - larguraObj:
        lixoPosiçãoX = 1026 - larguraObj
    return lixoPosiçãoX
def limparLinha():
    os.system("cls")