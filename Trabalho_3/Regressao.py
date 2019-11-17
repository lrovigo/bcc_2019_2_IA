import matplotlib.pyplot as plt
import numpy 
from statistics import mean 
import math  

def correlacao(Nx,Ny):

    media_x = (mean(Nx)) # calcula a media de x e y
    media_y = (mean(Ny))
    soma = 0.0
    soma_x = 0.0
    soma_y = 0.0
    r = 0.0
    soma2 = 0.0
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
    soma = 0.0
    soma_x = 0.0
    soma_y = 0.0
    x = 0.0
    y = 0.0
    
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
