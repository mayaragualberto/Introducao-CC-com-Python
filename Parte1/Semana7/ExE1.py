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

def n_primos(n):
    menor=2
    np=0
    while n>=menor:
        if éPrimo(n):
            np=np+1
            n=n-1
        else:
            n=n-1
    if n<menor:
        return np
    if n<0:
        print("Ops, número inválido!")

