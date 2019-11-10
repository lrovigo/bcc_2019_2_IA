import matplotlib.pyplot as plt
import numpy as np
from statistics import mean 
import math  

x1 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 =  [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

x2 = [10,8,13,9,11,14,6,4,12,7,5]
y2 = [9.14, 8.14, 8.47, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]

x3 = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 19]
y3 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 5.56, 7.91, 6.89, 12.50]

def main():
    print(correlacao(x1,y1))    

def correlacao(Nx,Ny):

    media_x = (mean(Nx))
    media_y = (mean(Ny))
    soma = 0
    soma_x = 0
    soma_y = 0
    for i in range(len(Nx)):
        x = (Nx[i] - media_x)
        y = (Ny[i] - media_y)
        soma += x * y
        
    for i in range(len(Nx)):
        soma_x += (Nx[i] - media_x)**2
        soma_y += (Ny[i] - media_y)**2
    soma_2 = math.sqrt(soma_x * soma_y)    

    r = soma / soma_2
    return r

def regressao():
    print('regrediu')
    
    
if __name__ == '__main__':
    main()
