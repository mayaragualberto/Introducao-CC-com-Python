class Triangulo:
    def __init__(self,a,b,c):
        self.a  =a
        self.b  =b
        self.c  =c

    def tipo_lado(self):
        if self.a != self.b and self.a!=self.c and self.b != self.c:
            return "escaleno"
        if self.a == self.b and self.a==self.c and self.b == self.c:
            return "equilátero"
        else:
            return "isósceles"
    
