def menor_nome(nomes):
    for pos in range(len(nomes)):
        nome_1=len(nomes[pos].strip())
        nome_2=len(nomes[pos+1].strip())
        if nome_1 < nome_2:
            menor = nomes[pos].strip().capitalize()
            return menor
        if nome_1 == nome_2:
            menor = nomes[pos].strip().capitalize()
            return menor
        else:
            menor = nomes[pos+1].strip().capitalize()
            return menor
        pos+=1
