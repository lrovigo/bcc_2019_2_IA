# Gabriel Garcia Salvador
# Gustavo Henrique Spiess
# Leonardo Rovigo
# Sidnei Lanser

#PERGUNTAS
# Aplique o kNN ao problema usando k = 1. Qual é a acurácia na classificação?
# R: A acuracia máxima é de 70.0% com 35 acertos e K = 1

# A acurácia pode ser igual a 92% com o kNN. Descubra por que o resultado atual é muito menor.
# Ajuste o conjunto de dados ou k de tal forma que a acurácia se torne 92% e explique o que você fez e
# por quê.
# R: Foi ajustado o K utlizando um while que calcula o Knn até passar pelo valor máximo possível
# com isso conseguimos uma acuracia de 96.0% com 48 acertos e K = 10 sem fazer a normalização

import interface
import numpy as np
from scipy.io import loadmat
def main():
    data_dict = loadmat('grupoDados3.mat') # carrega os dados para os dicionarios
    dadosTeste = data_dict['grupoTest']
    dadosTrain = data_dict['grupoTrain']
    data_testRots = data_dict['testRots']
    rotuloTrain = data_dict['trainRots']
    k = 1
    acuraciaMaxima = 0
    acuracia = 0
    rotuloPrevistoMax = []
    
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

    interface.visualizaPontos(dadosTeste,rotuloPrevistoMax,0,1) 
    print("Acuracia Máxima: " + str(100*acuraciaMaxima) + "%")
    print("Número de Acertos Máximo: " + str(numCorretoMaximo))
    print("Número Total: " + str(totalNum))
    print("O K melhor é: " + str(kMelhor))
    input()
            
if __name__ == "__main__" :
    main()
