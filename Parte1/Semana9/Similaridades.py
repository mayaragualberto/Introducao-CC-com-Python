import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))
    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
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

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i=0
    contador=0
    for i in range(len(as_a)):
        contador=(abs(as_a[i] - as_b[i]))+contador
        i=i+1
    return contador/6
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    numero_sentencas=0
    numero_frases=0
    numero_palavras=0
    numero_caracteres=0
    numero_caracteres_sentenca=0
    numero_caracteres_frase=0
    relacao_type_token=0
    razao_hapax_legomana=0
    lista_palavras=[]
    lista_palavras2=[] #Lista de cada palavra separada
    lista_palavras3=[] #Lista de todas as palavras separadamente
    caracter=[]
    lista_caracter=[]
    lista_sentencas=separa_sentencas(texto)
    numero_sentencas=len(lista_sentencas)
    for sentenca in lista_sentencas:
        numero_caracteres_sentenca=numero_caracteres_sentenca + len(sentenca)
        lista_frases=separa_frases(sentenca)
        numero_frases=len(lista_frases)+numero_frases
        for frase in lista_frases:
            numero_caracteres_frase=numero_caracteres_frase + len(frase) 
            lista_de_palavras=separa_palavras(frase)
            numero_palavras=len(lista_de_palavras)+numero_palavras # Até aqui tá certo, corrigir o restante
            for word in lista_de_palavras:
                lista_palavras2.append(word) # Lista com cada palavra separada
            for palavra in lista_de_palavras:
                lista_palavras3=palavra.split()
                for caracter in lista_palavras3:
                    y=0
                    while len(caracter)>y:
                        x=caracter[y]
                        y = y+1
                        lista_caracter.append(x)
    numero_caracteres=len(lista_caracter)
    
    numero_palavras_unicas=n_palavras_unicas(lista_palavras2) # Verifica dentro da lista de cada palavra separada
    numero_palavras_diferentes=n_palavras_diferentes(lista_palavras2) # Verifica dentro da lista de cada palavra separada
    
    tamanho_medio_palavras = numero_caracteres / numero_palavras # Funciona (5.571428571428571)
    relacao_type_token = numero_palavras_diferentes / numero_palavras # Funciona (0.8253968253968254)
    razao_hapax_legomana = numero_palavras_unicas / numero_palavras # Funciona (0.6984126984126984)
    tamanho_medio_sentenca = numero_caracteres_sentenca / numero_sentencas # Funciona (210.0)
    complexidade = numero_frases / numero_sentencas # Funciona (4.5) 
    tamanho_medio_frase = numero_caracteres_frase / numero_frases # Funciona (45.888)
    
    return [tamanho_medio_palavras, relacao_type_token, razao_hapax_legomana, tamanho_medio_sentenca, complexidade, tamanho_medio_frase]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturas = []
    for te in textos:
        assinaturas.append(calcula_assinatura(te))

    grauSimilaridade = 1000.0
    similar = 1
    
    for i in range( 0, len(textos)):
        similaridade = compara_assinatura(ass_cp, assinaturas[i])
        #print(similaridade)
        if (similaridade < grauSimilaridade):
            grauSimilaridade = similaridade
            similar = i + 1
    return similar

def main():
    assinatura=le_assinatura()
    textos=le_textos()
    copia=avalia_textos(textos,assinatura)
    return print("O autor do texto",copia,"está infectado com COH-PIAH")

main()



   
