#Recebe uma lista de números, remove os números repetidos e retorna os números em ordem crescentes

def remove_repetidos(lista):
    lentrada=[]
    for x in lista:
        if x not in lentrada:
            lentrada.append(x)
    lentrada.sort()
    return(lentrada)
