def soma_matrizes(m1, m2):
    numero_linhas_m1=len(m1)
    numero_colunas_m1=len(m1[0])
    numero_linhas_m2=len(m2)
    numero_colunas_m2=len(m2[0])

    matrizes_iguais=True
    soma_matrizes_m1_m2=[]

    if numero_linhas_m1 == numero_linhas_m2 and numero_colunas_m1 == numero_colunas_m2:
        for i in range(numero_linhas_m1):
            soma_matrizes_m1_m2.append([])
            for j in range(numero_colunas_m1):
                soma=m1[i][j] + m2[i][j]
                soma_matrizes_m1_m2[i].append(soma)

        resposta = soma_matrizes_m1_m2

        return resposta

    else:
        matrizes_iguais=False
        
        return matrizes_iguais
