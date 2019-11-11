import matplotlib.pyplot as plt
import numpy 
from statistics import mean 
import math  

x1 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 =  [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

x2 = [10,8,13,9,11,14,6,4,12,7,5]
y2 = [9.14, 8.14, 8.47, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]

x3 = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 19]
y3 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 5.56, 7.91, 6.89, 12.50]

def correlacao(Nx,Ny):

    media_x = (mean(Nx)) # calcula a media de x e y
    media_y = (mean(Ny))
    soma = numpy.int64(0)
    soma_x = numpy.int64(0)
    soma_y = numpy.int64(0)
    r = numpy.int64(0)
    numpy.int64(soma2)
    for i in range(len(Nx)):
        x = (Nx[i] - media_x) #x menos a media de x
        y = (Ny[i] - media_y) #y menos a media de y
        soma += x * y       # multiplicando os 2 resultados e somando na variavel soma
        
    for i in range(len(Nx)):
        soma_x += (Nx[i] - media_x)**2 #x menos a media de x tudo ao quadrado
        soma_y += (Ny[i] - media_y)**2 #y menos a media de y tudo ao quadrado
    soma_2 = math.sqrt(soma_x * soma_y)# raiz das somas acima

    r = soma / soma_2 # divisão das duas somatorias acima
    return r 

def regressao(Nx,Ny):
    media_x = (mean(Nx)) # calcula a media de x e y
    media_y = (mean(Ny)) 
    soma = numpy.int64(0)
    soma_x = numpy.int64(0)
    soma_y = numpy.int64(0)
    x = numpy.int64(0)
    y = numpy.int64(0)
    
    for i in range(len(Nx)): 
        x = (Nx[i] - media_x) #x menos a media de x
        y = (Ny[i] - media_y) #y menos a media de y
        soma += x * y
        
    for i in range(len(Nx)):
        soma_x += (Nx[i] - media_x)**2 #x menos a media de x tudo ao quadrado
        
    b1 = soma / soma_x # b1 é as duas somas acima
    b0 =  media_y - b1*media_x # b0 é a media de y menos b1 * a media de x
    return [b0,b1] # retornar um array com b0 e b1
    
if __name__ == '__main__':
    main()
