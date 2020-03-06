"""
todo/*------------------------------------------------------+
 | Projeto       | BLACKJACK                                |
 |----------------------------------------------------------|
 | Linguagem     | Python                                   |
 |----------------------------------------------------------|
 | Autor         | Lucas Matheus Rodrigues dos Santos       |
 |----------------------------------------------------------|
 | Módulo        | arquivo.py                               |
 +----------------------------------------------------------*/
"""

from dados import usuario


def arquivo_existe(arq):
    """
    :param arq: Nome de arquivo.
    :return: Diz se o arquivo exste ou não.
    """
    try:
        arquivo = open(arq, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(arq):
    """
    Cria um novo arquivo.
    :param arq: Nome do arquivo.
    """
    try:
        arquivo = open(arq, 'wt+')      # "wt" for write text
        arquivo.close()
    except FileExistsError:
        print('\033[31mHOUVE UM ERRO NA CRIÇÃO DO ARQUIVO\033[m')


def ler_arquivo(arq):
    """
    Lê um arquivo.
    :param arq: Nome do arquivo.
    :return: Retorna uma lista com todos os usuários.
    """
    usuarios = list()
    try:
        arquivo = open(arq, 'rt')  # "rt" for read text
    except FileNotFoundError:
        print('\033[31mNINGUÉM FOI CADASTRADO\033[m')
    else:
        usuarios = list()
        for linha in arquivo:
            usuario_info = linha.split(';')
            usuario = {'login': usuario_info[0],
                       'senha': usuario_info[1],
                       'nome': usuario_info[2],
                       'fichas': usuario_info[3].replace('\n', '')}
            usuarios.append(usuario)
    finally:
        return usuarios


def escrever_arquivo(arq, info):
    """
    Cadastra um usuário no arquivo.
    :param arq: Nome do arquivo.
    :param info: Informações do usuário.
    """
    login, senha, nome, fichas= info
    try:
        arquivo = open(arq, 'at')    # "at" for append text
    except:
        print('\033[31mHOUVE UM ERRO NO CADASTRO')
    else:
        arquivo.write(f'{login};{senha};{nome};{fichas}\n')
    finally:
        arquivo.close()


def apagar_usuario(arq, login):
    """
    Remove um usuário do arquivo.
    :param arq: Nome do arquivo.
    :param login: Login de identificação do usuário.
    """
    usuarios = ler_arquivo(arq)
    for pos, user in enumerate(usuarios):
        if login == user['login']:
            break
    del usuarios[pos]

    criar_arquivo(arq)
    for user in usuarios:
        user = usuario.Usuario(user['login'], user['senha'], user['nome'], user['fichas'])
        escrever_arquivo(arq, user.get_usuario())
