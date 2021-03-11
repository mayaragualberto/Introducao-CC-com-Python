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
                return True
                break
            b=b+1
        a=a+1
        b=a
    return False


def soma_hipotenusas(n):
    h=1
    soma=0
    while h<=n:
        hi=h*h       
        a=1
        b=1
        while a<n:
            while b<n:
                if hi==((a*a)+(b*b)):
                    soma=soma+h
                    a=n
                    break
                b=b+1
            a=a+1
            b=a
        h=h+1
    return soma  

    



        



