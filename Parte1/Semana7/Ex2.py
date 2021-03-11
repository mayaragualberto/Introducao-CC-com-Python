l=int(input("digite a largura: "))
a=int(input("digite a altura: "))

while a>0:
    m=l
    meio=False
    while meio==False:
        while m>0:
            print("#",end="")
            m=m-1
        meio=True
        a=a-1
    m=l
    print()
    m2=l
    while a>1 and meio:
        if m2==l:
            print("#",end="")
            m2=m2-1
        while m2==(l-1) or m2>1:
            print(" ",end="")
            m2=m2-1  
        print("#")
        m2=l
        a=a-1



