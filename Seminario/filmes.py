# Gabriel Garcia Salvador
# Gustavo Henrique Spiess
# Leonardo Rovigo
# Sidnei Lanser

import interface
from scipy.io import loadmat
import numpy as np
import random

dadosTeste = [[0,0,0,0,0]] # inicializa os dados de teste
oldDadosTrain = np.zeros((100,10)) # inicializa os dados de train que possuirão todas as notas dos 10 filmes
dadosTrain = np.zeros((100,5)) # inicialia os dados que possuirão os dados dos 5 filmes assistidos
rotuloTrain = np.zeros((100,1)) # inicializa o vetor de rótulos

def main():
    for i in range(len(oldDadosTrain)): #  preencher com notas aleatórias
        for j in range(len(oldDadosTrain[i])):
            oldDadosTrain[i][j] = random.randrange(10)

    for i in range(len(oldDadosTrain)): # preencher as 5 primeiras posições de dadosTrain com os valores de oldDadosTrain
        for j in range(5):
            dadosTrain[i][j] = oldDadosTrain[i][j]
            
    for i in range(len(rotuloTrain)): # preenchendo os rotulos
        rotuloTrain[i]= i
        
    print("Notas dos usuários dos 5 primeiros filmes :") # printando os usuários
    print(dadosTrain)
    
    nota_1 = input("Digite a nota 1:  ")
    nota_2 = input("Digite a nota 2:  ") 
    nota_3 = input("Digite a nota 3:  ") # obtendo as 5 notas
    nota_4 = input("Digite a nota 4:  ")
    nota_5 = input("Digite a nota 5:  ")
    
    dadosTeste[0][0] = int(nota_1)
    dadosTeste[0][1] = int(nota_2)
    dadosTeste[0][2] = int(nota_3) # colocando as 5 notas para teste
    dadosTeste[0][3] = int(nota_4)
    dadosTeste[0][4] = int(nota_5)

    k = 1 # definindo k como 1 pois iremos procurar apenas 1 usuário
    rotuloPrevisto = interface.meuKnn(dadosTrain, rotuloTrain,dadosTeste , k) # chamada para a funcao MeuKnn
    print("O Usuario com Gosto parecido é o número:")
    print(int(rotuloPrevisto[0] + 1)) # printando o numero do usuário 

    index = 0
    valoNotaMaxima = 0
    for i in range(len(oldDadosTrain[int(rotuloPrevisto[0])])):
        if(i >= 5):
            if(oldDadosTrain[int(rotuloPrevisto[0])][i] > valoNotaMaxima): # procurando o filme não assistido (i >= 5) com a nota mais alta para recomendar
                valoNotaMaxima = oldDadosTrain[int(rotuloPrevisto[0])][i]
                index = i

    print("Notas do usuário com gosto parecido: ")# printando as notas do usuário com gosto parecido
    print(oldDadosTrain[int(rotuloPrevisto[0])])
    
    print("Filme que é recomendado é o filme número:  ") # printando o filme não assistido com melhor nota
    print(index + 1)
    
    print("Com nota: ") # printando a nota do melhor filme
    print(valoNotaMaxima)
    input()
            
if __name__ == "__main__" :
    main()
