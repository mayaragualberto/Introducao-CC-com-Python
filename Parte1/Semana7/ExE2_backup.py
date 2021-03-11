import math

def é_hipotenusa(n):
    h=n
    soma=0
    hi=(h*h)       
    a=1
    b=1
    while (a<n):
        while (b<n):
            if (hi==((a*a)+(b*b))):
                a=n
                soma=soma+h
                return h
                break
            b=b+1
        a=a+1
        b=a
    return 0


def soma_hipotenusas(n):
    soma=0
    h=1
    while é_hipotenusa(n)<=n:
        soma=soma+h
    return soma   

    



        



