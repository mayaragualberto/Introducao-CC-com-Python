n=int(input("Digite um número inteiro: "))

primo=True
divisor=2
while n>0:
    while divisor<n and primo and n%divisor==0:
        if n%divisor==0:
            primo=False
        else:
            primo=True
        divisor=divisor+1
    if primo and n!=1:
        print("primo")
    else:
        print("não primo")
    divisor=2    
    n=int(input("Digite um número inteiro: "))
