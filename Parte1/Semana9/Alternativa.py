    for y in range
    for x in range(0,len(texto)): 
        saldo=texto[0] 
        while cont<len(saldo): 
            if saldo[cont] !=".": 
                numero_caracteres_sentenca += 1
                if saldo[cont] != ",":
                    numero_caracteres_frase +=1
            cont +=1
        sentenca=separa_sentencas(texto[x])
        for y in range(0,len(sentenca)):
            numero_sentencas += 1
            frase = separa_frases(sentenca[y])
            for z in range(0,len(frase)):
                numero_frases += 1
                palavra = separa_palavras(frase[z])
                for teste in palavra:
                    lista_palavras.append(teste)
                for w in range(0,len(palavra)):
                    numero_palavras += 1
                    numero_caracteres += len(palavra[w])
