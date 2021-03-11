class Triangulo:
    def __init__(self,a,b,c):
        self.a  =a
        self.b  =b
        self.c  =c

    def semelhantes(self,t2):
        semelhante = False
        if self.a//t2.a == 0 and self.b//t2.b == 0 and self.c//t2.c == 0:
            semelhante=True
            return semelhante
        if t2.a//self.a==0 and t2.b//self.b==0 and t2.c//self.c==0:
            semelhante=True
            return semelhante
        if self.a == t2.a and self.b==t2.b and self.c==t2.c:
            semelhante = True
            return semelhante            
        else:
            semelhante = False
            return semelhante

