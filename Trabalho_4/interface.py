# Gabriel Garcia Salvador
# Gustavo Henrique Spiess
# Leonardo Rovigo
# Sidnei Lanser
from scipy.io import loadmat

# data_dict = loadmat('Dados\data_preg.mat')# carregar o arquivo data_preg.mat
# data_dict = loadmat('Dados\data_preg.mat')# carregar o arquivo data_preg.mat
data_dict = loadmat('grupoDados1.mat')
dadosTeste = data_dict['grupoTest']
dadosTrain = data_dict['grupoTrain']
data_testRots = data_dict['testRots']
rotuloTrain = data_dict['trainRots']
# x = []
# y = []
# for i in range(len(data)):
#     x.append(data[i][0])
#     y.append(data[i][1])

def dist(dadosTeste, dadosTrain):
    return 
    pass

def meuKnn(dadosTrain, rotuloTrain, dadosTeste, k):
    
    for i in range(len(grupoTest)):
        delta = dist(dadosTeste, dadosTrain)

    pass

def visualizaPontos():
    pass

def normalizacao():
    pass


def main():
    

if __name__== "__main__" :
    main()