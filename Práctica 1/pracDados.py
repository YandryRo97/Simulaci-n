import random
import numpy as np
from prettytable import PrettyTable
import matplotlib.pyplot as plot

def main():
    
    resultado={}
    dados=[]
    frecuencia=[]
    
    for i in range(100000):
        dado1 = round(random.uniform(1, 6))
        dado2 = np.random.randint(1, 6)
        suma= dado1 + dado2
        if(bool(resultado.get(suma))== True):
            resultado[suma]=resultado.get(suma)+1
        else:
            resultado[suma]=1
    print(resultado)
    
   
    for m in list(resultado.keys()):
        dados.append(m)
    for n in list(resultado.values()):
        frecuencia.append(n)
        t = PrettyTable()
        t.field_names =['Dados','Frecuencia']
    for i in range(len(dados)):
        t.add_row([dados[i], frecuencia[i]])
        plot.hist(x=dados[i], bins=frecuencia[i], color='#F2AB6D', rwidth=0.85)
    print(t)

if __name__ == '__main__':
    main()