def imprime_matriz(minha_matriz):
    numero_linhas=len(minha_matriz)
    numero_colunas=len(minha_matriz[0])
    i=0
    j=0
    for i in range(numero_linhas):
        line=''
        for j in range(numero_colunas):
            line += f'{minha_matriz[i][j]}'
        print (' '.join(line),end='')
        print('')

