"""
todo/*------------------------------------------------------+
 | Projeto       | BLACKJACK                                |
 |----------------------------------------------------------|
 | Linguagem     | Python                                   |
 |----------------------------------------------------------|
 | Autor         | Lucas Matheus Rodrigues dos Santos       |
 |----------------------------------------------------------|
 | Módulo        | menu.py                                  |
 +----------------------------------------------------------*/
"""

from dados import banco_de_dados
from jogo import mesa
import recursos as r


def menu():
    """
    Menu principal
    """
    r.blackjack(0.5)
    r.printar(15)
    banco = banco_de_dados.BancoDeDados()

    while True:
        escolha = r.leia_int(f'{r.cor("roxo")}ESCOLHA UMA OPÇÃO:     [1] - FAZER LOGIN     [2] - CRIAR CONTA     '
                             f'[3] - SAIR DO JOGO\n\n{r.cor("azul")}OPÇÃO  ►►  ')

        if escolha == 1:
            r.printar(5)
            usuario = banco.fazer_login()
            r.printar(5)
            return menu_do_jogo(usuario)
        elif escolha == 2:
            usuario = banco.criar_conta()
            return menu_do_jogo(usuario)
        elif escolha == 3:
            exit()
        else:
            print(f'{r.cor("vermelho")}POR FAVOR, ESCOLHA UMA DAS OPÇÕES.{r.cor("normal")}')


def menu_do_jogo(usuario):
    while True:
        escolha = r.leia_int(f'{r.cor("roxo")}ESCOLHA UMA OPÇÃO:     [1] - JOGAR     [2] - LOGOUT'
                             f'\n\n{r.cor("azul")}OPÇÃO  ►►  ')

        if escolha == 1:
            mesa.Mesa(usuario).iniciar_jogo()
        elif escolha == 2:
            r.printar(30)
            return menu()
        else:
            print(f'{r.cor("vermelho")}POR FAVOR, ESCOLHA UMA DAS OPÇÕES.{r.cor("normal")}')




menu()