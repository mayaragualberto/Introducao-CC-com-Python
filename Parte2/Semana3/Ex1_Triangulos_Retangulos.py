class Triangulo:
    def __init__(self,a,b,c):
        self.a  =a
        self.b  =b
        self.c  =c

    def retangulo(self):
        retangulo = False
        if self.a**2==self.b**2+self.c**2: 
            retangulo=True
            return retangulo
        if self.b**2==self.c**2+self.a**2:
            retangulo=True
            return retangulo
        if self.c**2==self.a**2+self.b**2:
            retangulo=True
            return retangulo
        if (self.a == self.b == self.c):
            retangulo=False
            return retangulo
        else:
            retangulo=False
            return retangulo
    
