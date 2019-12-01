# Gabriel Garcia Salvador
# Gustavo Henrique Spiess
# Leonardo Rovigo
# Sidnei Lanser

#PERGUNTAS
# Aplique seu kNN a este problema. Qual é a sua acurácia de classificação?
# R: A acuracia máxima é de 78.33% com 47 acertos e K = 10

# A acurácia pode ser igual a 98% com o kNN. Descubra por que o resultado atual é muito menor.
# Ajuste o conjunto de dados ou k de tal forma que a acurácia se torne 98% e explique o que você fez e
# por quê.
# R: Foi visto que o menor e maior valor tinham uma diferença enorme entre si então foi aplicada a normalização
# para colocar os valores entre 0 e 1 porem ainda só conseguimos uma acurácia de 91.666% com 55 acertos e K = 4
# nesse exercício foi aplicado um while para verificar qual o melhor K possível

import interface
import numpy as np
from scipy.io import loadmat
def main():
    data_dict = loadmat('grupoDados2.mat') # carrega os dados para os dicionarios
    dadosTeste = data_dict['grupoTest']
    dadosTrain = data_dict['grupoTrain']
    data_testRots = data_dict['testRots']
    rotuloTrain = data_dict['trainRots']
    rotuloPrevistoMax = []
    k = 1
    acuraciaMaxima = 0
    acuracia = 0
    
    for r in range(len(dadosTeste)): # fazer a normalização dos dados de teste
        dadosTeste[r] = interface.normalizacao(dadosTeste[r])

    for s in range(len(dadosTrain)):# fazer a normalização dos dados de treino
        dadosTrain[s] = interface.normalizacao(dadosTrain[s])
    
    while (acuracia != 100 and k <= len(dadosTrain)): # while para verificar qual o melhor K possível
        numCorreto = 0
        rotuloPrevisto = interface.meuKnn(dadosTrain, rotuloTrain, dadosTeste, k) # chamada para a funcao MeuKnn
        for i in range(len(rotuloPrevisto)): # for para somar a o numero de acertos
            if(rotuloPrevisto[i] == data_testRots[i]):
                numCorreto += 1
        
        totalNum = len(data_testRots) # total de valores
        acuracia = numCorreto / totalNum # numero de acertos
        if(acuracia > acuraciaMaxima): # verifica se a acuracia atual e maior que a maxima obtida
            acuraciaMaxima = acuracia # se for grava a acuracia como maxima
            numCorretoMaximo = numCorreto # grava o numero de acertos
            kMelhor = k # grava o melhor K
            rotuloPrevistoMax = rotuloPrevisto
            
        k += 1
        
    interface.visualizaPontos(dadosTeste,rotuloPrevistoMax,1,2) 
    print("Acuracia Máxima: " + str(100*acuraciaMaxima) + "%")
    print("Número de Acertos Máximo: " + str(numCorretoMaximo))
    print("Número Total: " + str(totalNum))
    print("O K melhor é: " + str(kMelhor))
    input()
            
if __name__ == "__main__" :
    main()
