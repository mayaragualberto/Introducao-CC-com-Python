tamanho=int(input("Digite a quantidade de números da sequência: "))

produto=1

i=0

while i<tamanho:
    valor=int(input("Digite um valor a ser somado: "))
    produto=produto*valor
    i=i+1
print("O produto dos valores digitados é: ", produto)
