def partida():
    n=float(input("Quantas peças? "))
    m=float(input("Limite de peças por jogada? "))
    if n%(m+1)==0:
        usuario_escolhe_jogada(n,m)
    else:
        computador_escolhe_jogada(n,m)

def campeonato(p):
    if p==0:
        partida()
    while p==1 or  p<=3:
        print("**** Rodada", p," ****","\n")
        partida()
        p=p+1
    if p==4:
        print("**** Final do campeonato! ****","\n")
        print("Placa: Você 0 x 3 Computador")

def computador_escolhe_jogada(n,m):
    print("Computador começa!","\n")
    cn=1
    n=n-cn
    while cn<m or n%(m+1)!=0:
        cn=cn+1
        if n%(m+1)==0:
            n=n-cn
    if cn==1 and n%(m+1)==0 and n!=0:
        return("O computador tirou uma peça.")
        print("Agora restam",n,"peças no tabuleiro.","\n")
        usuario_escolhe_jogada(n,m)
    if cn>1 and n%(m+1)==0 and n!=0:
        return("O computador tirou",cn,"peças.")
        print("Agora restam",n,"peças no tabuleiro.","\n")
        usuario_escolhe_jogada(n,m)
    if n==0:
        return("O computador tirou uma peça.")
        print("Fim do jogo! O computador ganhou!","\n")
    if n<=m:
        cn=n+1
        return("O computador tirou",cn,"peças.")
        print("Fim do jogo! O computador ganhou!","\n")

def usuario_escolhe_jogada(n,m):
    print("Voce começa!","\n")
    un=float(input("Quantas peças você vai tirar? "))
    n2=n-un
    #n2 é o resto após a escolha de un
    while un>=n or un>m:
    #caso o resto da jogada seja maior ou igual ao resto do jogo
    #ou o número escolhido seja maior que o limite
        print("\t")
        print("Oops! Jogada inválida! Tente de novo.","\n")
        un2=int(input("Quantas peças você vai tirar? "))
        un=un2
    if n2==1:
    #caso o resto seja igual a 1 e o número escolhido seja maior que um
        n2=n-un
        n=n2
        print("Você tirou",un,"peças.")
        print("Agora resta apenas uma peça no tabuleiro.","\n")
        computador_escolhe_jogada(n,m)
    if n2!=1 and un>1:
    #caso o resto seja diferente de 1 e o número escolhido seja maior que um
        n2=n-un
        n=n2
        return("Você tirou",un,"peças.")
        print("Agora restam",n2,"peças no tabuleiro.","\n")
        computador_escolhe_jogada(n,m)
    if n2==1 and un==1:
    #caso o resto seja igual a um e o número escolhido seja um
        n2=n-un
        n=n2
        return("Você tirou uma peça.")
        print("Agora resta apenas uma peça no tabuleiro.","\n")
        computador_escolhe_jogada(n,m)
    if n2!=1 and un==1:
    #caso o resto seja diferente de 1 e o número escolhido seja 1
        n2=n-un
        n=n2
        return("Você tirou uma peça.")
        print("Agora restam",n2,"peças no tabuleiro.","\n")
        computador_escolhe_jogada(n,m)

def jogo():
    print("Bem-vindo ao jogo do NIM! Escolha:","\n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato 2")
    pc=float(input())
    p=1
    if pc==1:
        print("Voce escolheu uma partida isolada!","\n")
        p=0
        partida()
    else:
        print("Voce escolheu um campeonato!","\n")
        p=1
        campeonato(p)
    
jogo()
