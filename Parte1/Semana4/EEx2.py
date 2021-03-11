n=int(input("Digite um número inteiro: "))

nIgual=False
nRest=n%10
n=n//10

while nIgual==False and n>0:	
	nRest1=n%10  
	n=n//10
	if nRest1==nRest:
		nIgual=True
	nRest=nRest1
if nIgual==True:
	print("sim")
else: 
	print("não")

