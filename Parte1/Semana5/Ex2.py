def eprimo(t):
    eprimo=True
    divisor=2
    while divisor<t and eprimo:
        resto=t%divisor
        if resto==0:
            eprimo=False
        divisor=divisor+1
    if eprimo and t!=1:
        return True
    else:
        return False

def maior_primo(t):
    x=t
    eprimo(x)==False
    while not eprimo(x):
        x=x-1
    if eprimo(x)==True:
        return x
    
def test_primo():
    assert maior_primo(35)==31

def test_primo():
    assert maior_primo(100)==97

def test_primo():
    assert maior_primo(35)==31

    
    


