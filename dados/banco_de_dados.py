"""
todo/*------------------------------------------------------+
 | Projeto       | BLACKJACK                                |
 |----------------------------------------------------------|
 | Linguagem     | Python                                   |
 |----------------------------------------------------------|
 | Autor         | Lucas Matheus Rodrigues dos Santos       |
 |----------------------------------------------------------|
 | Módulo        | banco_de_dados.py                        |
 +----------------------------------------------------------*/
"""

from dados import arquivos, usuario
import recursos


class BancoDeDados(object):
    """
    Classe que registra e acessa todos os usuários do arquivo.
    """
    __arq = 'usuarios.txt'

    def __init__(self):
        if not arquivos.arquivo_existe(self.__arq):
            arquivos.criar_arquivo(self.__arq)

    def get_arquivo(self):
        return self.__arq

    def criar_conta(self):
        """
        Cria uma nova conta no arquivo.
        :return: Retorna o novo usuário e todas as suas informações.
        """
        print(F'{"CRIANDO PERFIL":^30}')
        while True:
            login = recursos.leia_dados('login: ', 5)
            if not self.__conta_existe(login):
                if login.lower() != 'new login':
                    break
                print(f'{login} não pode ser um login!\nPor favor, digite um usuário válido.')
            else:
                print('Esse usuário já existe!\nPor favor, digite um usuário válido.')
        senha = recursos.leia_dados('Senha: ', 8)
        nome = recursos.leia_nome('nome: ')

        user = usuario.Usuario(login, senha, nome)
        arquivos.escrever_arquivo(self.__arq, user.get_usuario())
        return user

    def __conta_existe(self, login):
        """
        Verifica se a conta passada existe.
        :param login: Verifica de acordo com o login se há um determinado usuário no arquivo.
        :return: True caso exista ou False caso não exista.
        """
        usuarios = arquivos.ler_arquivo(self.__arq)
        for user in usuarios:
            if user['login'].lower() == login.lower():
                return True
        return False

    def __mostrar_usuarios(self):
        """
        Mostra uma lista com todos os usuários.
        Pode ser usada em testes.
        """
        users = arquivos.ler_arquivo(self.__arq)
        [print(users[i], '\n') for i in range(0, len(users))]

    def fazer_login(self):
        """
        Realiza o acesso à conta do usuário.
        :return: Retorna o usuário que acessou e suas informações.
        """
        print(F'{"FAZENDO LOGIN":^50}')
        recursos.printar(5)
        users = arquivos.ler_arquivo(self.__arq)

        user = object
        while True:
            while True:
                login = recursos.leia_dados('Login: ', 5)
                if self.__conta_existe(login):
                    break
                print('Conta inexistente')

            while True:
                senha = recursos.leia_dados('\nsenha ["new login" para tentar outro usuário]: ', 8)
                validacao = False

                if senha.lower() == 'new login':
                    break

                for n in range(0, len(users)):
                    user = users[n]
                    if user['login'] == login:
                        if user['senha'] == senha:
                            validacao = True
                            break
                        break

                if validacao:
                    break

                print('LOGIN OU SENHA INVÁLIDOS, POR FAVOR TENTE NOVAMENTE')

            if senha.lower() != 'new login':
                break
        user = usuario.Usuario(user['login'], user['senha'], user['nome'], user['fichas'])
        return user
