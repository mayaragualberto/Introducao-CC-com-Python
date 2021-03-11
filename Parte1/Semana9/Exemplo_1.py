import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))
    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas

def tamanho_medio_palavra (n_total_caracter, n_total_palavras): # Tamanho médio de palavra é o total de caractéres dividido pelo número total de palavras.
    tamanho_palavra = n_total_caracter / n_total_palavras
    return tamanho_palavra

def tamanho_medio_sentença(n_total_caracter_sentença, n_total_sentenças):# Tamanho médio de sentença é o total de caracteres dividido pelo número de sentenças
    tamanho_sentença= n_total_caracter_sentença/ n_total_sentenças
    return tamanho_sentença

def complexidade_sentença(n_total_frases, n_total_sentenças):# Complexidade de sentença é o número total de frases divido pelo número de sentenças.
    comp_sentença = n_total_frases/n_total_sentenças
    return comp_sentença

def tamanho_medio_frase(n_total_caracter_frase, n_total_frases):# Tamanho médio de frase é o total de caracteres dividido pelo número de frases no texto 
    tamanho_frase= n_total_caracter_frase/n_total_frases
    return tamanho_frase

def type_token(n_total_palavras, l_palavra): #Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. 
    n_p_d = n_palavras_diferentes(l_palavra)
    token = n_p_d / n_total_palavras
    return token

def razão_hapax (n_total_palavras, l_palavra):# Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras 
    n_p_u = n_palavras_unicas(l_palavra)
    hapax = n_p_u / n_total_palavras
    return hapax

def calcula_assinatura(texto):
    n_total_sentenças=0
    n_total_frases=0
    n_total_palavras=0
    n_total_caracter=0
    n_total_caracter_sentença = 0 ## Novidade
    n_total_caracter_frase = 0 ## Novidade
    as_x=[]
    lista_caracter =[]
    l_palavra=[]
    ls_palavra=[]
    lista_sentença =separa_sentencas(texto) # Listas do texto com sentenças separadas (em cada item)
    n_total_sentenças=len(lista_sentença)
    for sentença in lista_sentença:
        n_total_caracter_sentença += len(sentença) ## Novidade
        lista_frase = separa_frases(sentença) # Listas de sentenças com frases separadas (em cada item)
        n_total_frases=len(lista_frase)+n_total_frases
        for frase in lista_frase:
            n_total_caracter_frase += len(frase) ## Novidade
            lista_palavra = separa_palavras(frase) # listas de frases com as palavras separadas (em cada item)
            n_total_palavras=len(lista_palavra)+n_total_palavras
            for word in lista_palavra:
                l_palavra.append(word) # lista de palavra separadas 
            for palavra in lista_palavra:
                ls_palavra=palavra.split() # Varias listas com uma palavra em cada.
                for caracter in ls_palavra:
                    y=0
                    while len(caracter)>y:
                        x=caracter[y]
                        y=y+1
                        lista_caracter.append(x)
    n_total_caracter = len(lista_caracter)
    n_total_caracter_com_espaço= (len(texto))-1
    as_x=[tamanho_medio_palavra (n_total_caracter, n_total_palavras), type_token(n_total_palavras, l_palavra), razão_hapax (n_total_palavras, l_palavra),tamanho_medio_sentença(n_total_caracter_sentença, n_total_sentenças), complexidade_sentença(n_total_frases, n_total_sentenças), tamanho_medio_frase(n_total_caracter_frase, n_total_frases)]
    return as_x

def compara_assinatura(as_a, as_b): #Essa funcao recebe 2 assinaturas de texto e devolve o grau de similaridade nas assinaturas
    soma =0
    x =0
    for item in as_a:
        soma = abs(as_a[x] - as_b[x]) + soma
        x = x + 1
    comparativo = soma/6
    return comparativo 

def avalia_textos(textos, ass_cp): #Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.
    mais_provavel=0
    n_texto=0
    semelhança=0
    for texto in textos:
        semelhança_2 = compara_assinatura(calcula_assinatura (texto), ass_cp)
        n_texto +=1
        if semelhança > semelhança_2 :
            mais_provavel=n_texto
        semelhança= semelhança_2
    return mais_provavel

def inicio():
    assinatura = le_assinatura()
    textos = le_textos()
    matriz_ass = calcula_assinatura(textos)
    ass_comparadas = compara_assinatura(assinatura, matriz_ass)
    copiah = avalia_textos(textos, ass_comparadas) + 1
    return print("O autor do texto", copiah, "está infectado com COH-PIAH.")

inicio()
