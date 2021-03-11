def soma_matrizes(m1, m2):

# preencher primeiro as colunas

    nlinhas1 = len(m1)

    ncolunas1 = len(m1[0])

    nlinhas2 = len(m2)

    ncolunas2 = len(m2[0])
    
    m3 = []

    if nlinhas1 == nlinhas2 and ncolunas1 == ncolunas2:

        for i in range(nlinhas1):

            m3.append([])

            for j in range(ncolunas1):

                soma = m1[i][j] + m2[i][j]

                m3[i].append(soma)

        resposta = "soma matrizes(m1, m2) => " + str(m3)
        return resposta

    else:

        resposta = "soma matrizes(m1, m2) => False"
    
        return print(resposta)
