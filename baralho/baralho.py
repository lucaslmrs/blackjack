"""
todo/*------------------------------------------------------+
 | Projeto       | BLACKJACK                                |
 |----------------------------------------------------------|
 | Linguagem     | Python                                   |
 |----------------------------------------------------------|
 | Autor         | Lucas Matheus Rodrigues dos Santos       |
 |----------------------------------------------------------|
 | Módulo        | baralho.py                               |
 +----------------------------------------------------------*/
"""

from baralho.cartas import Carta
from random import shuffle


class Baralho(object):
    """
    Representa um baralho no jogo.
    """
    def __init__(self):
        self.novo_baralho()

    def embaralhar(self):
        shuffle(self.baralho)

    def novo_baralho(self):
        """
        Adiciona todas as cartas no baralho.
        """
        self.baralho = list()
        naipes = ('♠', '♥', '♦', '♣')
        for naipe in naipes:
            for i in range(1, 14):
                if i == 1:
                    self.baralho.append(Carta('A', naipe, (1, 11)))
                elif i == 11:
                    self.baralho.append(Carta('J', naipe, 10))
                elif i == 12:
                    self.baralho.append(Carta('Q', naipe, 10))
                elif i == 13:
                    self.baralho.append(Carta('K', naipe, 10))
                else:
                    self.baralho.append(Carta(i, naipe, i))

    def __str__(self):
        """
        Forma que um baralho é mostrado caso solicitado.
        :return: Retorna um string com todas as informações das cartas presentes no baralho
        """
        show = str()
        for c in self.baralho:
            show += str(c) + '\n'
        return show

    def puxar(self):
        """
        Retira uma carta do baralho.
        :return: Retorna uma carta.
        """
        return self.baralho.pop()
