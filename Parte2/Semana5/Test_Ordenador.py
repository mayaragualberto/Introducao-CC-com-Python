import Ordenador_2
import pytest
import ContaTempos

class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return Ordenador_2.Ordenador()

    @pytest.fixture
    def l_quase(self):
        c= ContaTempos.ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleat(self):
        c= ContaTempos.ContaTempos()
        return c.lista_aleatoria(100)

    def esta_ordenada(self,l):
        for i in range(len(l)-1):
            if l[i]>l[i+1]:
                return False
        return True

    def test_bolha_curta_aleat(self,o,l_aleat):
        o.bolha_curta(l_aleat)
        assert self.esta_ordenada(l_aleat)

        
