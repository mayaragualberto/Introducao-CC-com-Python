def sao_multiplicaveis(m1, m2):
    numero_linhas_m1=len(m1)
    numero_colunas_m1=len(m1[0])
    numero_linhas_m2=len(m2)
    numero_colunas_m2=len(m2[0])

    matrizes_iguais=True

    if numero_colunas_m1 == numero_linhas_m2:
        matrizes_iguais=True

        return matrizes_iguais

    else:
        matrizes_iguais=False
        
        return matrizes_iguais
