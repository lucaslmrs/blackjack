"""
todo/*------------------------------------------------------+
 | Projeto       | BLACKJACK                                |
 |----------------------------------------------------------|
 | Linguagem     | Python                                   |
 |----------------------------------------------------------|
 | Autor         | Lucas Matheus Rodrigues dos Santos       |
 |----------------------------------------------------------|
 | Módulo        | mesa.py                                  |
 +----------------------------------------------------------*/
"""

import jogo.jogador as jogador
import jogo.dealer as dealer
import recursos as r
from dados import banco_de_dados, arquivos
from time import sleep


class Mesa(object):
    """
    Mesa é um objeto no qual ocorre o jogo
    """
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__jogador = jogador.Jogador(self.__usuario.nome, self.__usuario.fichas)
        self.__dealer = dealer.Dealer()

    def iniciar_jogo(self):
        """
        Representa cada partida.
        :return: Não possui.
        """
        r.printar(15)
        print(f'{r.cor("roxo")}=-=' * 30)
        r.printar(13)
        bem_vindo = f'{self.__usuario.nome.upper()} BEM VINDO AO BLACKJACK'.split()
        [(print(palavra, end=' '), sleep(0.4)) for palavra in bem_vindo]
        r.printar(7)
        while True:
            self.__jogador.reiniciar()
            self.__dealer.reiniciar()
            self.__rodada()
            self.__registrar_rodada()

            continuar = r.leia_string(f'{r.cor("roxo")}Deseja continuar?? [S/N]: {r.cor("normal")}')[0] in 'Ss'
            if not continuar:
                r.printar(15)
                break

    def __rodada(self):
        """
        Representa cada rodada de uma partida.
        :return: Não possui
        """
        r.printar(5)
        self.__jogador.definir_aposta(f'{r.cor("verde")}Digite o valor de sua aposta: ')
        r.printar(5)

        self.__dar_cartas()

        self.__jogador.mostrar(self.__dealer)

        if self.__verif_seguro():
            return

        msg = f'{r.cor("verde")}MAO1: ESCOLHA UMA OPÇÃO:     [1] - PEDIR CARTA     [2] - PARAR     ' \
              f'[3] - DOBRAR APOSTA\n\n\nOPÇÃO  ►►  '

        #   Caso possa realizar uma divisão.
        dividir = False
        if self.__jogador.mao['mao1'][0].dados['carta'] == self.__jogador.mao['mao1'][1].dados['carta']:
            dividir = r.leia_string(f'{r.cor("verde")}Deseja dividir?[S/N]: ') in 'Ss'
            if dividir:
                self.__jogador.dividir(self.__dealer, msg)
                self.__dealer.revelar()
                if not self.__blackjack(False):
                    self.__calcular_fichas('mao1')
                if not self.__blackjack(False, 'mao2'):
                    self.__calcular_fichas('mao2')

        #   Caso não ocorra divisão, segue o jogo.
        if not dividir:
            self.__jogador.opções_de_jogo(self.__dealer, msg, True, 'mao1')
            self.__dealer.jogada_dealer(self.__jogador, 'mao1')
            self.__dealer.revelar()
            self.__calcular_fichas('mao1')

    def __registrar_rodada(self):
        """
        Registra as fichas do jogador no arquivo de texto.
        :return: Não possui.
        """
        b = banco_de_dados.BancoDeDados()
        arquivos.apagar_usuario(b.get_arquivo(), self.__usuario.login)
        self.__usuario.fichas = self.__jogador.fichas
        arquivos.escrever_arquivo(b.get_arquivo(), self.__usuario.get_usuario())

    def __verif_seguro(self):
        """
        Caso possa pedir um seguro, pergunta-se ao jogador se ele deseja um.
        :return: Chama a função blackjack e retorna se a partida acabou ou não.
        """
        seguro = False
        if self.__dealer.mao[0].dados['carta'] == 'A':
            print(f'\n{self.__jogador.nome}:      {self.__jogador.mostrar(self.__dealer)}')
            seguro = r.leia_string(f'{r.cor("verde")}Deseja fazer um seguro?[S/N]: ') in 'Ss'
            if seguro:
                self.__jogador.definir_seguro()

        return self.__blackjack(seguro)

    def __blackjack(self, seguro, mao='mao1'):
        """
        verifica se há algum blackjack na mesa, se sim, calculasse as fichas e encerra a rodada.
        :param seguro: Diz se o jogador fez um seguro.
        :return: Indica o fim ou não da partida.
        """
        black_dealer = self.__is_blackjack(self.__dealer.mao)
        black_player = self.__is_blackjack(self.__jogador.mao[mao])
        fim = False
        if black_dealer or black_player:
            fim = True
            for letra in 'B  L  A  C  K  J  A  C  K\n\n':
                if '\n' != letra != ' ':
                    sleep(0.25)
                print(f'{r.cor("vermelho")}{letra}', end='')
            print(f'{r.cor("normal")}')
            if black_dealer and black_player:
                print('ISSO É DIFICIL DE VER!')
                print(f'FICHAS: {self.__jogador.fichas} + {int(self.__jogador.aposta[mao])}')
                self.__jogador.fichas += int(self.__jogador.aposta[mao])
            elif black_dealer:
                if self.__dealer.mao[0].dados['carta'] == 'A':
                    if seguro:
                        print('SORTE QUE COMPROU UM SEGURO NÉ KKK')
                        print(f'FICHAS: {self.__jogador.fichas} + {int(self.__jogador.aposta[0] * (3 / 2))}')
                        self.__jogador.fichas += int(self.__jogador.aposta[0] * (3 / 2))
                    else:
                        print(f'FICHAS: {self.__jogador.fichas} - {int(self.__jogador.aposta[mao])}')
                        print('AGORA SE ARREPENDEU DE NÃO TER FEITO O SEGURO NÉ?')
            elif black_player:
                print('PARABÉNS!!!')
                print(f'FICHAS: {self.__jogador.fichas} + {int(self.__jogador.aposta[0] * (5 / 2))}')
                self.__jogador.fichas += int(self.__jogador.aposta[0] * (5 / 2))
        r.printar(3)
        return fim

    @staticmethod
    def __is_blackjack(cartas):
        """
        verifica se é blackjack.
        :param cartas:
        :return: True para quando é blackjack e False quando não é.
        """
        return r.contar_pontos(cartas) == 21 and len(cartas) == 2

    def __calcular_fichas(self, mao):
        """
        Calcula o valor das fichas de acordo com o resultado da rodada.
        :param mao: verifica qual jogo está no momento com o jogador.
        """
        vencedor = self.__vencedor(mao)

        print(f'{mao}: VENCEDOR DA RODADA  ->  {vencedor}')

        if mao == 'mao1':
            mao = 0
        else:
            mao = 1

        f = self.__jogador.fichas
        a = self.__jogador.aposta[mao]
        if vencedor == 'jogador':
            print(f'FICHAS: {f} + {int(a * 2)} = {f + a * 2}')
            self.__jogador.fichas += int(a * 2)
        elif vencedor == 'dealer':
            print(f'FICHAS: {f} + 0 = {f}')
            pass
        elif vencedor == 'empate':
            print(f'FICHAS: {f} + {a} = {f + a}')
            self.__jogador.fichas += a
        r.printar(3)

    def __vencedor(self, num_mao):
        """
        :param num_mao: verifica qual jogo está no momento com o jogador.
        :return: Diz quem é o vencedor da rodada
        """
        pts_dealer = r.contar_pontos(self.__dealer.mao)
        pts_jogador = r.contar_pontos(self.__jogador.mao[num_mao])

        if pts_dealer < pts_jogador:
            if pts_jogador <= 21:
                return 'jogador'
            else:
                return 'dealer'
        elif pts_dealer > pts_jogador:
            if pts_dealer <= 21:
                return 'dealer'
            else:
                return 'jogador'
        else:
            return 'empate'

    def __dar_cartas(self):
        """
        Dá as cartas no início da partida
        :return:
        """
        self.__jogador.pedir_carta(self.__dealer)
        self.__dealer.puxar_carta()
        self.__jogador.pedir_carta(self.__dealer)
        self.__dealer.puxar_carta()
