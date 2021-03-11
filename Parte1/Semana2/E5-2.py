numInt=input("Digite um número inteiro: ")

num=int(numInt)

unid=num % 10

num1=(num-unid) / 10

digDez=int(num1%10)


print("O dígito das dezenas é", digDez)
