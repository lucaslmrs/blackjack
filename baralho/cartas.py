"""
todo/*------------------------------------------------------+
 | Projeto       | BLACKJACK                                |
 |----------------------------------------------------------|
 | Linguagem     | Python                                   |
 |----------------------------------------------------------|
 | Autor         | Lucas Matheus Rodrigues dos Santos       |
 |----------------------------------------------------------|
 | Módulo        | cartas.py                                |
 +----------------------------------------------------------*/
"""

class Carta(object):
    """
    Classe que representa uma carta no jogo.
    """
    def __init__(self, carta, naipe, valor):
        self.dados = {'carta': carta, 'naipe': naipe, 'valor': valor, 'verso': '◘'}

    def mostrar(self, revelar=False):
        """
        Mostra a carta.
        :param revelar: Caso True, mostra a carta e o naipe dela. Caso False, mostra apenas o verso da carta.
        :return: Retorna as informações da carta.
        """
        if revelar:
            return f'{self.dados["carta"]}{self.dados["naipe"]}'
        else:
            return self.dados['verso']

    def __str__(self):
        """
        Forma em que a carta é mostrada caso solicitada.
        :return: Retorna uma string com as informações da carta.
        """
        return f"[{self.dados['carta']} {self.dados['naipe']} -- {self.dados['valor']} -- {self.dados['verso']}]"
