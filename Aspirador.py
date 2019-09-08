import matplotlib.pyplot as plt
from random import randint
currLine = 1
currCol = 4
direcao = ''
def main():
    global currLine
    global currCol
    
    numeroSugeiras = randint(1,16)
    numeroSugeirasRestantes = numeroSugeiras
    matriz = [[1,1,1,1,1,1],[1,0,0,0,0,1],[1,0,0,0,0,1],[1,0,0,0,0,1],[1,0,0,0,0,1],[1,1,1,1,1,1]] #Trocar Para Json
    preencherMatriz(matriz,numeroSugeiras)
    exibir(matriz)
    global direcao
    direcao = 'DIREITA'
    direcaoY = 'BAIXO'
    while numeroSugeirasRestantes > 0:
        if(matriz[currLine][currCol] == 2):
            agenteReativoSimples(matriz[currLine][currCol])
            matriz[currLine][currCol] = 0
           
        if (currCol < len(matriz)-2 and direcao == 'DIREITA') or (currCol > 1 and direcao == 'ESQUERDA'):
            agenteReativoSimples(matriz[currLine][currCol])
            moverDirecao(direcao)    
        else:
            if(currLine < len(matriz)-2 and direcaoY == 'BAIXO') or (currLine > 1 and direcaoY == 'CIMA'):
                aux = direcao
                direcao = direcaoY
                agenteReativoSimples(matriz[currLine][currCol])
                direcao = aux
                moverDirecao(direcaoY)
                if(direcaoY == 'BAIXO' and currLine == len(matriz)-2):
                    direcaoY = 'CIMA'
                else:
                    if direcaoY == 'CIMA' and currLine == 1:
                        direcaoY = 'BAIXO'
                if(direcao == 'DIREITA'):
                    direcao = 'ESQUERDA'
                else:
                    direcao = 'DIREITA'
            else:
                if(currLine == len(matriz)-2 and direcaoY == 'BAIXO'):
                    direcaoY = 'CIMA'
        exibir(matriz)

def exibir(matriz):
    global currLine
    global currCol
    plt.imshow(matriz, 'gray')
    plt.show(block=False)
    plt.plot(currCol, currLine, '*r', 'LineWidth', 5)
    plt.pause(0.5)
    plt.clf()

def preencherMatriz(matriz,numeroSugeiras):
    while numeroSugeiras > 0:
        coluna = randint(0,5)
        linha = randint(0,5)
        if(matriz[linha][coluna] == 0):
            matriz[linha][coluna] = 2
            numeroSugeiras = numeroSugeiras - 1

def moverDirecao(direcao):
    if direcao == 'DIREITA':
        moverDireita()
        return
        
    if direcao == 'ESQUERDA':
        moverEsquerda()
        return
        
    if direcao == 'CIMA':
        moverCima()
        return
        
    if direcao == 'BAIXO':
        moverBaixo()
        return
        
def moverDireita():
    global currCol
    currCol = currCol +1
        
def moverEsquerda():
    global currCol
    currCol = currCol - 1
        
def moverBaixo():
    global currLine
    currLine = currLine + 1    
        
def moverCima():
    global currLine
    currLine = currLine - 1       

def agenteReativoSimples(percepcao):
    global direcao
    if percepcao == 0:
        print('Estado da percepcao: 0 Acao escolhida:' + direcao)
        return direcao
            
    if percepcao == 2:
        print('Estado da percepcao: 2 Acao escolhida: ASPIRAR')
        return 'ASPIRAR'

if __name__ == "__main__":
    main()

        
        
