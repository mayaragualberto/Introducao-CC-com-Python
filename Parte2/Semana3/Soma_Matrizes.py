import Matriz

def soma_matrizes (A,B):
    num_linhas=len(A)
    num_colunas=len(A[0])
    C=Matriz.cria_matriz(num_linhas,num_colunas,0)

    for lin in range(num_linhas):
        for col in range(num_colunas):
            C[lin][col]=A[lin][col]+B[lin][col]
    return C

if __name__ == '__main__':
    A=[[1,2,3],[4,5,6],[7,8,9]]
    B=[[10,20,30],[40,50,60],[70,80,90]]
    print(soma_matrizes(A,B))
