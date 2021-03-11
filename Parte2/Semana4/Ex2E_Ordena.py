def ordena(lista):
    fim=len(lista)
    for i in range (fim-1):
        pos_min=i

        for j in range(i+1,fim):
            if lista[j]<lista[pos_min]:
                pos_min=j

        lista[i],lista[pos_min]=lista[pos_min],lista[i]
    return lista
