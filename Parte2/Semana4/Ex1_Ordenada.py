def ordenada(lista):
    fim = len(lista)
    lista_ordem = lista[:]
    for i in range(fim-1):
        posicao_do_minimo = i
        for j in range(i+1,fim):
            if lista_ordem[j] < lista_ordem[posicao_do_minimo]:
                posicao_do_minimo = j
        lista_ordem[i], lista_ordem[posicao_do_minimo] = lista_ordem[posicao_do_minimo], lista_ordem[i]
    ordenada = True
    if lista == lista_ordem:
        return ordenada
    else:
        ordenada = False
        return False
