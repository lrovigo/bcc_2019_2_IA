# Gabriel Garcia Salvador
# Gustavo Henrique Spiess
# Leonardo Rovigo
# Sidnei Lanser
from scipy.io import loadmat
import math
import numpy as np
from scipy.stats import mode
import matplotlib.pyplot as plt

def dist(dadoTeste, dadoTrain):
    soma = 0
    for i in range(len(dadoTeste)): # para cada valor da linha do dado de treino
        soma += (dadoTeste[i] - dadoTrain[i])**2 # aplicar a somatoria da formula da distancia
    return math.sqrt(soma) #terminar a formula com a aplicação da raiz quadrada
    
def meuKnn(dadosTrain, rotuloTrain, dadosTeste, k):
    tamnhoTeste = len(dadosTeste)
    tamanhoTrain = len(dadosTrain)
    distanciasIndex = np.zeros((tamnhoTeste,tamanhoTrain)) # Criar matriz tamnhoTeste * tamanhoTrain que conterá os index's
    distancias = np.zeros((tamnhoTeste,tamanhoTrain)) #Criar matriz tamnhoTeste * tamanhoTrain
    
    for i in range(len(dadosTeste)): # para cada elemento nos dados de teste
        for j in range(len(dadosTrain)):    # para cada elemento nos dados de treino 
            y = dadosTrain[j] # pegar a linha do dado de teste
            x = dadosTeste[i] # pegar a linha do dado de treino
            distancias[i][j] = dist(x, y); #calcular a distancia
            
        lista_ordenada =  sorted(list(enumerate(distancias[i])), key=lambda x: x[1])# transformar o array em um lista de tuplas com o format = "(indice,valor)" e ordenar pelo valor
        for l in range(len(lista_ordenada)): #para cada valor da lista ordenada
            distanciasIndex[i][l] = lista_ordenada[l][0] #pegar o index do valor
    
    rotulosIndex = np.zeros((tamnhoTeste,k)) # criar uma matriz tamnhoTeste * k
    rotulosPrevistos = [] # criar array dos rotulos previstos
    for n in range(len(distanciasIndex)):  # para cada valor na matriz de indexes
        indexes = [] # criar um array que sera usado para pegar apenas os "k" primeiros valores onde "k" é um valor passado como parametro para esta funcao
        for m in range(k): 
            indexes.append(distanciasIndex[n][m]) # adicionar os "k" primeiros valores
            
        for o in range(len(indexes)):
            rotulosIndex[n][o] = rotuloTrain[int(indexes[o])][0] # procurar os valores dos "k" primeros nos rotulos de treino

        rotulosPrevistos.append(mode(rotulosIndex[n])[0][0]) # adicionar no array de rotulos previstos, executando a funcao "mode" pegando sempre a primeira moda
    return rotulosPrevistos



