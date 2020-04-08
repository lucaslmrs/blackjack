"""
todo/*------------------------------------------------------+
 | Projeto       | BLACKJACK                                |
 |----------------------------------------------------------|
 | Linguagem     | Python                                   |
 |----------------------------------------------------------|
 | Autor         | Lucas Matheus Rodrigues dos Santos       |
 |----------------------------------------------------------|
 | Módulo        | jogador.py                               |
 +----------------------------------------------------------*/
"""

import recursos as r


class Jogador(object):
    """
    Essa classe representa um jogador durante a partida.
    """
    def __init__(self, nome, fichas):
        self.nome = nome
        self.fichas = int(fichas)
        self.aposta = [int(), int()]
        self.seguro = 0
        self.mao = {'mao1': list(), 'mao2': list()}

    def reiniciar(self):
        self.aposta = [int(), int()]
        self.seguro = 0
        self.mao = {'mao1': list(), 'mao2': list()}

    def definir_aposta(self, msg):
        """
        Define o valor inicial da aposta.
        :param msg: mensagem que será mostrada ao usuário quando a função for solicitada.
        """
        self.aposta[0] = r.leia_int(msg)

        if self.aposta[0] > self.fichas:
            self.definir_aposta('\033[0;31mVocê não possui fichas o suficiente. '
                                'Por favor, digite um valor válido: \033[m')
        elif self.aposta[0] < 20:
            self.definir_aposta('\033[0;31mO mínimo valor possível pra apostas é 20. '
                                'Por favor, digite um valor válido: \033[m')
        elif self.aposta[0] % 10 != 0:
            self.definir_aposta('\033[0;31mPor favor, digite um valor válido múltiplo de 10: \033[m')
        else:
            self.fichas -= self.aposta[0]

    def dividir(self, dealer, msg):
        """
        Divide o jogo do jogador em dois jogos.
        :param dealer: Recebe o dealer do jogo com suas informações.
        :param msg: Mensagem que será exibida ao usuário.
        """
        self.mao['mao2'].append(self.mao['mao1'].pop())
        self.aposta = (self.aposta[0], self.aposta[0])

        self.opções_de_jogo(dealer, msg, True, 'mao1')
        self.opções_de_jogo(dealer, msg, True, 'mao2')

    def definir_seguro(self):
        self.seguro = int(self.aposta[0] * (3 / 2))
        self.fichas -= int(self.aposta[0] / 2)

    def opções_de_jogo(self, dealer, msg, dobrar=True, num_mao='mao1'):
        """
        Pergunta ao jogador o que ele vai fazer na rodada.
        :param dealer: Contém as informações do dealer.
        :param msg: Mensagem que será exibida ao usuário.
        :param dobrar: Verifica se pode dobrar ou não.
        :param num_mao: Recebe o jogo atual do jogador.
        """
        r.printar(3)
        self.mostrar(dealer)

        if r.contar_pontos(self.mao[num_mao]) < 21:
            escolha = r.leia_int(msg)
            if escolha == 1:
                self.pedir_carta(dealer, num_mao)
                msg = num_mao.upper() + f'{r.cor("verde")}: ESCOLHA UMA OPÇÃO:     [1] - PEDIR CARTA    [2] - PARAR' \
                                        f'\n\n\nOPÇÃO  ►►  '
                self.opções_de_jogo(dealer, msg, False, num_mao)
            if escolha == 2:
                self.parar()
            if escolha == 3 and dobrar:
                self.dobrar_aposta(dealer, num_mao)
                self.mostrar(dealer)
        r.printar(2)

    def pedir_carta(self, dealer, num_mao='mao1'):
        self.mao[num_mao].append(dealer.dar_carta())

    def dobrar_aposta(self, dealer, num_mao='mao1'):
        num = 0
        if num_mao == 'mao2':
            num = 1
        self.aposta[num] *= 2
        self.pedir_carta(dealer, num_mao)

    def parar(self):
        """
        Encerra a jogada.
        """
        pass

    def mostrar(self, dealer):
        """
        Mostra a Situação atual do jogo
        """
        print(f'{r.cor("roxo")}=-=' * 30)
        r.printar(10)
        print(f'{r.cor("amarelo")}jogador: {self.nome.upper()} =-= fichas: {self.fichas}\t\t '
              f'APOSTA: {str(self.aposta)}\n\n')
        dealer.mostrar()
        print()
        for num_mao, jogo in self.mao.items():
            if len(jogo) > 0:
                print(f'{r.cor("verde")}{num_mao.upper()}:', end='     ')
                for carta in jogo:
                    print(f"{r.cor('verde')} {carta.mostrar(True)}", end=' →')
                print(f'→→►\t\t{r.cor("azul")}{r.contar_pontos(self.mao[num_mao])} pontos{r.cor("normal")}')
        r.printar(5)
