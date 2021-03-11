def é_vogal(frase):
    acumulador =''
    for caracter in frase:
        if caracter in 'AEIOUaeiou':
            acumulador=acumulador+caracter
    return acumulador

def é_consoante(frase):
    acumulador =''
    vogais=len(é_vogal(frase))
    for caracter in frase:
        if caracter in ' ':
            acumulador=acumulador+caracter
    sem_espaço=len(acumulador)
    consoante= len(frase) - sem_espaço - vogais
    return consoante

def conta_letras(frase,contar="vogais"):
    if contar == "vogais":
        acumulador=len(é_vogal(frase))
        return acumulador
    if contar == "consoantes":
        consoante=é_consoante(frase)
        return consoante
    else:
        return len(frase)

