Num=int(input("Digite um número inteiro: "))

Num2=Num%3

Num3=Num%5

if Num2==0 and Num3==0:
	print("FizzBuzz")
else:
	print(Num)
