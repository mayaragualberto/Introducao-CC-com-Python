def encontra_impares(lista,lista1=[]):
    if len(lista) == 1:
        if lista[0] % 2 != 0:
            return lista
        else:
            return lista1
    else:
        if len(lista) > 1:
            if lista[0] % 2 != 0:
                return [lista[0]] + encontra_impares(lista[1:])
            else:
                return encontra_impares(lista[1:])
