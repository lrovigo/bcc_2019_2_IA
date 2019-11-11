from Regressao import correlacao,regressao
from scipy.io import loadmat

data_dict = loadmat('Dados\data.mat') # carregar o arquivo data.mat
data = data_dict.get('data') # pegar apenas os dados relevantes

data_dict2 = loadmat('Dados\data_preg.mat')# carregar o arquivo data_preg.mat
data2 = data_dict2.get('data') # pegar apenas os dados relevantes


