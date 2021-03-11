def é_caracter_maiusculo(caracter):
    maiuscula=range(65,91)
    if ord(caracter) in maiuscula:
        return caracter

def maiusculas(frase):
    maiuscula=range(65,91)
    acumulador=''
    for caracter in frase:
        if é_caracter_maiusculo(caracter):
            acumulador=acumulador+caracter
    return acumulador 
