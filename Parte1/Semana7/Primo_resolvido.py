def éPrimo(x):
    fator=2
    if x==2:
        return True
    while x%fator!=0 and fator<=x/2:
        fator=fator+1
    if x%fator==0:
        return False
    else:
        return True

def primo():
    n=int(input("Digite um número inteiro: "))
    while n>0:
        if éPrimo(n):
            print(n,"é primo! :-)")
        else:
            print(n,"não é primo! :-(")
        n=int(input("Digite um número inteiro: "))
    if n<0:
        print("Ops, número inválido!")
        n=int(input("Digite um número inteiro: "))
primo()
