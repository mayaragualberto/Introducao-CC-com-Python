import random

def lista_grande(n):
    lista=[]
    cont=0
    while cont < n:
        elemento_aleatório=random.randint(-2*n,2*n)
        lista.append(int(elemento_aleatório))
        cont+=1
    return lista
