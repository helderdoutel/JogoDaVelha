import random
from os import system, name


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

    def mostrar_tabuleiro(self):
        """."""
        for x in range(3):
            print(" %s | %s | %s" % (
                self._tabuleiro[x][0],
                self._tabuleiro[x][1],
                self._tabuleiro[x][2]))

    def jogar(self, jogador, x, y):
        """."""
        self._tabuleiro[x][y] = jogador
        return True


def clear():
    """."""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
t = Tabuleiro(1, 2)
jogador = random.randint(1, 2)
print("Jogador %s começa" % str(jogador))
while not t.vencedor():
    print("Vez do jogador %d" % jogador)
    t.mostrar_tabuleiro()
    temp = input("Jogar em qual posição(xy)? ")
    t.jogar(jogador, int(temp[0]) - 1, int(temp[1]) - 1)
    clear()
    jogador = (jogador % 2) + 1
print("Jogador %d ganhou" % t.vencedor())
t.mostrar_tabuleiro()
