# Gabriel Garcia Salvador
# Gustavo Henrique Spiess
# Leonardo Rovigo
# Sidnei Lanser
from scipy.io import loadmat
import math
import numpy as np


# data_dict = loadmat('Dados\data_preg.mat')# carregar o arquivo data_preg.mat
# data_dict = loadmat('Dados\data_preg.mat')# carregar o arquivo data_preg.mat
data_dict = loadmat('grupoDados1.mat')
dadosTeste = data_dict['grupoTest']
dadosTrain = data_dict['grupoTrain']
data_testRots = data_dict['testRots']
rotuloTrain = data_dict['trainRots']


def dist(dadosTeste, dadosTrain):
    return 
    pass

def meuKnn(dadosTrain, rotuloTrain, dadosTeste, k):
    
    distancias = np.eye(len(dadosTeste),len(dadosTrain)) #Criar matriz 50*100
    soma = 0
    for i in range(len(dadosTeste)): # para cada elemento nos dados de teste
        for j in range(len(dadosTrain)):    # para cada elemento nos dados de treino 
            y = dadosTeste[i] # pegar a linha do dado de teste
            x = dadosTrain[j] # pegar a linha do dado de treino
            for k in range(len(x)): # para cada valor da linha do dado de treino
                soma += (x[k] - y[k])**2 # aplicar a somatoria da formula da distancia
            distancias[i][j] = math.sqrt(soma); #terminar a formula com a aplicação da raiz quadrada
            soma = 0
        distancias[i] = np.sort(distancias[i]) # ordenar o alinha e colocar na matriz

    pass

def visualizaPontos():
    pass

def normalizacao():
    pass


def main():
    k = 3
    meuKnn(dadosTrain, rotuloTrain, dadosTeste, k)

            
    
if __name__ == "__main__" :
    main()
