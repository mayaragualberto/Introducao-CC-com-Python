def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    comp = False
    if n%(m+1) == 0:
        print()
        print("Voce começa!")
    else:
        print()
        print("Computador começa!")
        comp = True
    while n > 0:
        if comp:
            cn = computador_escolhe_jogada(n, m)
            n=n-cn
            if cn == 1:
                print()
                print("O computador tirou uma peça")
            else:
                print()
                print("O computador tirou", cn, "peças")
            comp = False
        else:
            un=usuario_escolhe_jogada(n, m)
            n=n-un
            if un==1:
                print("\t")
                print("Você tirou uma peça")
            else:
                print()
                print("Você tirou", un, "peças")
            comp=True
        if n==1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print("\t")
        else:
            if n != 0:
                print("Agora restam", n, "peças no tabuleiro.")
                print("\t")
    print("Fim do jogo! O computador ganhou!")


def computador_escolhe_jogada(n, m):
    cn = 1
    #caso o número escolhido seja diferente do limite
    while cn!=m:
        #o o resto deve ser múltiplo de m+1
        if (n-cn)%(m+1)==0:
            return cn
        else:
            cn=cn+1
    return cn

def usuario_escolhe_jogada(n,m):
    podeun = False
    while not podeun:
        un=int(input("Quantas peças você vai tirar? "))
        #enquanto o número for inválido
        if un>m or un<1:
            print("\t")
            print("Oops! Jogada inválida! Tente de novo.")
            print("\t")
        else:
            podeun = True
    return un


def campeonato():
    part = 1
    #enquanto o campeonato não faz a rodada 3
    while part<=3:
        print("\t")
        print("**** Rodada", part, "****")
        print("\t")
        partida()
        part=part+1
    print("\t")
    print("Placar: Você 0 X 3 Computador")

def jogo():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("\t")
    print("1 - para jogar uma partida isolada")
    pc=int(input("2 - para jogar um campeonato "))
    if pc==2:
        print("\t")
        print("Voce escolheu um campeonato!")
        print("\t")
        campeonato()
    else:
        if pc == 1:
            print("\t")
            partida()

jogo()
