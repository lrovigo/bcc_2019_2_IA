from Regressao import correlacao,regressao
from plotter import plot_dot,show,plot_line
import matplotlib.pyplot as plt

def calc(reg,x,y):
    result = []
    print(reg[0])
    print(reg[1])
    for i in range(len(x)):
        print(x[i])
        print(y[i])
        x2 = (y[i] - reg[0])/reg[1]   # X = Y - b0/b1  
        y2 = reg[0] + (reg[1] * x[i]) # Y = b0 + b1X
        result.append([x2,y2])
        
    return result    

def plot(x,y):
    vetor = []
    for i in range(len(x)):
        vetor.append([x[i],y[i]])

    plot_dot(vetor, c='m', label = 'testing')

    corr = correlacao(x,y)
    reg = regressao(x,y)
    plot_line(calc(reg,x,y), c='r')   
    print(reg)
    print(corr)
    

x1 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 =  [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

x2 = [10,8,13,9,11,14,6,4,12,7,5]
y2 = [9.14, 8.14, 8.47, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]

x3 = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 19]
y3 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 5.56, 7.91, 6.89, 12.50]


plot(x1,y1)
show()

plot(x2,y2)
show()

plot(x3,y3)
show()
