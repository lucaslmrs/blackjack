"""
todo/*------------------------------------------------------+
 | Projeto       | BLACKJACK                                |
 |----------------------------------------------------------|
 | Linguagem     | Python                                   |
 |----------------------------------------------------------|
 | Autor         | Lucas Matheus Rodrigues dos Santos       |
 |----------------------------------------------------------|
 | Módulo        | recursos.py                              |
 +----------------------------------------------------------*/
"""
from random import randint
from time import sleep
from baralho.cartas import Carta


def leia_string(msg):
    try:
        frase = str(input(msg)).strip()
    except (ValueError, TypeError):
        print('\033[0;31mTivemos um problema com o tipo que você digitou.\033[m')
        return leia_string('\033[0;31mPor favor, digite direito:\033[m ')
    except KeyboardInterrupt:
        print('\033[0;31mO usuário preferiu não informar os dados.\033[m')
        return 0
    else:
        return frase


def leia_nome(msg='Digite seu nome: '):
    import string
    nome = leia_string(msg)
    isvalido = True

    if len(nome) < 3:
        return leia_nome('\033[0;31mPor favor, digite um nome com mais de 3 caracteres:\033[m ')

    for letra in nome:
        if letra not in string.ascii_letters and letra not in ' ':
            isvalido = False

    if not isvalido:
        return leia_nome('\033[0;31mPor favor, digite apenas letras:\033[m ')
    return nome


def leia_int(msg):
    try:
        num = int(input(msg))
    except (ValueError, TypeError):
        print('\033[0;31mTivemos um problema com o tipo que você digitou.\033[m')
        return leia_int('\033[0;31mPor favor, digite um número válido:\033[m ')
    except KeyboardInterrupt:
        print('\033[0;31mO usuário preferiu não informar os dados.\033[m')
        return 0
    else:
        return int(num)


def leia_dados(msg, min_caract=5):
    """
    Usado para ler logins e senhas.
    :param msg: Mensagem mostrada ao usuário.
    :param min_caract: Caracteres mínimos para realizar a operação.
    :return: Retorna o dado que a função foi chamada para receber.
    """
    dado = leia_string(msg)
    if len(dado) < min_caract:
        return leia_string(f'\033[0;31mPor favor, digite mais de {min_caract} caracteres:\033[m ')
    return dado


def contar_pontos_ases(num_ases, pontos):
    pontos_em_aberto = 21 - pontos
    ases_pontos = 0
    for n in range(num_ases):
        if n == num_ases - 1:
            if pontos_em_aberto >= 11:
                ases_pontos += 11
                pontos_em_aberto - 11
                continue
        ases_pontos += 1
        pontos_em_aberto -= 1
    return ases_pontos


def contar_pontos(cartas):
    """
    Conta os pontos das cartas presentes numa mão.
    :param cartas: Cartas presentes numa mão
    :return: Quantidade de pontos.
    """
    pontos = 0
    ases = 0
    for carta in cartas:
        if carta.dados['carta'] == 'A':
            ases += 1
        else:
            pontos += carta.dados['valor']

    return pontos + contar_pontos_ases(ases, pontos)


def printar(n):
    [print() for i in range(0, n)]

color = {'normal': '\033[m',  # 0 - Sem cores
         'vermelho': '\033[0;31m',  # 1 - Vermelho
         'verde': '\033[0;32m',  # 2 - Verde
         'amarelo': '\033[0;33m',  # 3 - Amarelo
         'azul': '\033[0;34m',  # 4 - Azul
         'roxo': '\033[0;35m',  # 5 - Roxo
         'branco': '\033[7;30m'}  # 6 - Branco


def cor(num):
    return color[num]


def blackjack(tempo):
    """
    Imprime a palavra BLACKJACK grande e com cores.
    :param tempo: tempo que será exibido cada linha.
    """
    c = list(color.keys())[(randint(1, 5))]
    print(f'{cor(c)}')
    print('╔ ═ ═ ═ ╗   ╔           ╔ ═ ═ ═ ╗   ╔ ═ ═ ═ ╗   ╔     ╗   ╔ ═ ═ ═ ╗   ╔ ═ ═ ═ ╗   ╔ ═ ═ ═ ╗    ╔     ╗')
    sleep(tempo)
    print('║       ║   ║           ║       ║   ║           ║   ╝             ║   ║       ║   ║            ║   ╝  ')
    sleep(tempo)
    print('║ ═ ═ ═ ╣   ║           ╠ ═ ═ ═ ╣   ║           ╠ ═               ║   ╠ ═ ═ ═ ╣   ║            ╠ ═    ')
    sleep(tempo)
    print('║       ║   ║           ║       ║   ║           ║   ╗     ╚       ╝   ║       ║   ║            ║   ╗  ')
    sleep(tempo)
    print('╚ ═ ═ ═ ╝   ╚ ═ ═ ═ ╝   ╚       ╝   ╚ ═ ═ ═ ╝   ╚     ╝     ╚ ═ ╝     ╚       ╝   ╚ ═ ═ ═ ╝    ╚     ╝')
    print(f'{cor("normal")}')
