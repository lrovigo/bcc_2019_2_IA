# Gabriel Garcia Salvador
# Gustavo Henrique Spiess
# Leonardo Rovigo
# Sidnei Lanser

# PERGUNTAS:
# Qual é a acurácia máxima que você consegue da classificação?
# R: A acuracia máxima é de 98.0% com 49 acertos e K = 3

# É necessário ter todas as características (atributos) para obter a acurácia máxima para esta
# classificação?
# R: Sim, pois os dados se referem aos tamanhos das partes das flores, remover um desses
# atributos pode causar impacto na acuracia

import interface
from scipy.io import loadmat

data_dict = loadmat('grupoDados1.mat') # carrega os dados para os dicionarios
dadosTeste = data_dict['grupoTest']
dadosTrain = data_dict['grupoTrain']
data_testRots = data_dict['testRots']
rotuloTrain = data_dict['trainRots']

def main():
    k = 3
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

    interface.visualizaPontos(dadosTeste,rotuloPrevistoMax,1,2) 
    print("Acuracia Máxima: " + str(100*acuraciaMaxima) + "%")
    print("Número de Acertos Máximo: " + str(numCorretoMaximo))
    print("Número Total: " + str(totalNum))
    print("O K melhor é: " + str(kMelhor))
    input()
            
if __name__ == "__main__" :
    main()
