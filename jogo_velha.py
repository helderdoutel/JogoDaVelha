# import random


class Tabuleiro:
    """."""

    def __init__(self, jogador1=None, jogador2=None):
        """."""
        self._jogador1 = jogador1
        self._jogador2 = jogador2
        self._tabuleiro = self.reset_tabuleiro()

    def reset_tabuleiro(self):
        """."""
        tabuleiro = []
        for x in range(3):
            tabuleiro.append([0, 0, 0])
        return tabuleiro

    def get_tabuleiro(self):
        """."""
        return self._tabuleiro

    def vencedor(self):
        """Retorna jogador vencedor do jogo. linha coluna."""
        vencedor = 0
        # coluna
        for x in range(3):
            temp = []
            for y in range(3):
                if self._tabuleiro[x][y] not in temp:
                    temp.append(self._tabuleiro[x][y])
            if len(temp) == 1:
                vencedor = temp[0]
        # linha
        for x in range(3):
            temp = []
            for y in range(3):
                if self._tabuleiro[y][x] not in temp:
                    temp.append(self._tabuleiro[y][x])
            if len(temp) == 1:
                vencedor = temp[0]
        # diagonal 1
        temp = []
        for x in range(3):
            if self._tabuleiro[x][x] not in temp:
                temp.append(self._tabuleiro[x][x])
        if len(temp) == 1:
            vencedor = temp[0]

        # diagonal 2
        temp = []
        for x in range(3):
            if self._tabuleiro[x][(x - 2) * (-1)] not in temp:
                temp.append(self._tabuleiro[x][(x - 2) * (-1)])
        if len(temp) == 1:
            vencedor = temp[0]
        return vencedor

t = Tabuleiro(1, 2)
print(t.get_tabuleiro())
