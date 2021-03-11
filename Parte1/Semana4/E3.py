n=int(input("Digite um número inteiro: "))

soma=0

while  n>0:
	nRest=n%10
	n=(n-nRest)/10
	soma=soma+nRest

print(soma)
