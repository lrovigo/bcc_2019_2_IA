from Regressao import correlacao,regressao
from scipy.io import loadmat
import numpy
from plotter import plot_line

data_dict = loadmat('Dados\data_preg.mat')# carregar o arquivo data_preg.mat
data = data_dict.get('data') # pegar apenas os dados relevantes
x = []
y = []
for i in range(len(data)):
    x.append(data[i][0])
    y.append(data[i][1])

n1 = numpy.polyfit(x,y,1)
plot_line(result,'r')

n2 = numpy.polyfit(x,y,2)
plot_line(result, 'g')

n3 = numpy.polyfit(x,y,3)
plot_line(result, 'b')

n8 = numpy.polyfit(x,y,8)
plot_line(result, 'y')
 
