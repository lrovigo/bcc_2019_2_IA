# Gabriel Garcia Salvador
# Gustavo Henrique Spiess
# Leonardo Rovigo
# Sidnei Lanser
from scipy.io import loadmat
import math
import numpy as np
from scipy.stats import mode


# data_dict = loadmat('Dados\data_preg.mat')# carregar o arquivo data_preg.mat
# data_dict = loadmat('Dados\data_preg.mat')# carregar o arquivo data_preg.mat
data_dict = loadmat('grupoDados1.mat')
dadosTeste = data_dict['grupoTest']
dadosTrain = data_dict['grupoTrain']
data_testRots = data_dict['testRots']
rotuloTrain = data_dict['trainRots']

def dist(dadoTeste, dadoTrain):
    soma = 0
    for i in range(len(dadoTeste)): # para cada valor da linha do dado de treino
        soma += (dadoTeste[i] - dadoTrain[i])**2 # aplicar a somatoria da formula da distancia
    return math.sqrt(soma) #terminar a formula com a aplicação da raiz quadrada
    
def meuKnn(dadosTrain, rotuloTrain, dadosTeste, k):
    distanciasIndex = np.zeros((50,100)) # Criar matriz 50*100 que conterá os index's
    distancias = np.zeros((50,100)) #Criar matriz 50*100
    
    for i in range(len(dadosTeste)): # para cada elemento nos dados de teste
        for j in range(len(dadosTrain)):    # para cada elemento nos dados de treino 
            y = dadosTrain[j] # pegar a linha do dado de teste
            x = dadosTeste[i] # pegar a linha do dado de treino
            distancias[i][j] = dist(x, y); 
            
        lista_ordenada =  sorted(list(enumerate(distancias[i])), key=lambda x: x[1])# transformar o array em um lista de tuplas com o format = "(indice,valor)" e ordenar pelo valor
        for l in range(len(lista_ordenada)): #para cada valor da lista ordenada
            distanciasIndex[i][l] = lista_ordenada[l][0] #pegar o index do valor
    
    rotulosIndex = np.zeros((50,k)) # criar uma matriz 50*k
    rotulosPrevistos = [] # criar array dos rotulos previstos
    for n in range(len(distanciasIndex)):  # para cada valor na matriz de indexes
        indexes = [] # criar array que sera usado para pegar apenas os "k" primeiros valores onde "k" é um valor passado como parametro
        for m in range(k): 
            indexes.append(distanciasIndex[n][m]) # adicionar os "k" primeiros valores
            
        for o in range(len(indexes)):
            rotulosIndex[n][o] = rotuloTrain[int(indexes[o])] # procurar os valores dos "k" primeros nos rotulos de treino

        rotulosPrevistos.append(mode(rotulosIndex[n])[0][0]) # adicionar no array de rotulos previstos, executando a funcao "mode" pegando sempre a primeira moda

    return rotulosPrevistos
        
    
def visualizaPontos():
    pass

def normalizacao():
    pass


def main():
    k = 1
    numCorreto = 0
    rotuloPrevisto = meuKnn(dadosTrain, rotuloTrain, dadosTeste, k)
    for i in range(len(rotuloPrevisto)):
        if(rotuloPrevisto[i] == data_testRots[i]):
            numCorreto += 1
    
    totalNum = len(data_testRots)
    acuracia = numCorreto / totalNum
    
    print("Acuracia: " + str(100*acuracia) + "%")
    print("Número de Acertos: " + str(numCorreto))
    print("Número Total: " + str(totalNum))

            
if __name__ == "__main__" :
    main()
