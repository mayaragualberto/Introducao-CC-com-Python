import math
X1=int(input("Digite a coordenada x do primeiro ponto: "))
Y1=int(input("Digite a coordenada y do primeiro ponto: "))

X2=int(input("Digite a coordenada x do segundo ponto: "))
Y2=int(input("Digite a coordenada y do segundo ponto: "))

D= math.sqrt(((X1-X2)**2)+((Y1-Y2)**2))

if D>10:
	print("longe")
else:
	print("perto")


