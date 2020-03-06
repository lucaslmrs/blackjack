"""
todo/*------------------------------------------------------+
 | Projeto       | BLACKJACK                                |
 |----------------------------------------------------------|
 | Linguagem     | Python                                   |
 |----------------------------------------------------------|
 | Autor         | Lucas Matheus Rodrigues dos Santos       |
 |----------------------------------------------------------|
 | Módulo        | dealer.py                                |
 +----------------------------------------------------------*/
"""

from time import sleep
from baralho import baralho
import recursos as r


class Dealer(object):
    """
    Representa um dealer na partida.
    """
    def __init__(self):
        self.baralho = baralho.Baralho()
        self.baralho.embaralhar()
        self.mao = list()

    def dar_carta(self):
        return self.baralho.puxar()

    def puxar_carta(self):
        self.mao.append(self.dar_carta())

    def __deve_puxar(self, jogador, num_mao):
        """
        Verifica se o dealer deve puxar uma carta ou não.
        :param jogador: Recebe as informações do jogador.
        :param num_mao: Passa o jogo atual do jogador.
        :return: True para puxar e False para não puxar
        """
        pts_oponente = r.contar_pontos(jogador.mao[num_mao])
        if pts_oponente <= 21:
            pts_dealer = r.contar_pontos(self.mao)
            if pts_dealer >= 21:
                False
            elif pts_dealer < pts_oponente:
                return True
            elif pts_dealer == pts_oponente:
                if pts_dealer < 15:
                    return True
                else:
                    return False
        return False

    def mostrar(self):
        """
        Mostra o jogo inicial do dealer.
        """
        print('Dealer:', end='\t\t')
        print(f"{self.mao[0].mostrar(True)} → {self.mao[1].mostrar(False)}")

    def revelar(self):
        """
        Mostra o jogo final do dealer.
        """
        print(f'{r.cor("roxo")}{"JOGADA DO DEALER":^40}')
        print('Dealer:', end='\t\t')
        for carta in self.mao:
            print(f" {carta.mostrar(True)}", end=' →')
            sleep(1)
        print(f'→→► {r.cor("vermelho")}\t{r.contar_pontos(self.mao)} pontos\n\n{r.cor("normal")}')

    def jogada_dealer(self, jogador, num_mao):
        """
        Realiza todas as jogadas do dealer na rodada.
        :param jogador: Recebe as informções do jogador.
        :param num_mao: Jogo atual do jogador.
        """
        while self.__deve_puxar(jogador, num_mao):
            self.mao.append(self.dar_carta())
