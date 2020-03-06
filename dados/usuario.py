"""
todo/*------------------------------------------------------+
 | Projeto       | BLACKJACK                                |
 |----------------------------------------------------------|
 | Linguagem     | Python                                   |
 |----------------------------------------------------------|
 | Autor         | Lucas Matheus Rodrigues dos Santos       |
 |----------------------------------------------------------|
 | Módulo        | usuario.py                               |
 +----------------------------------------------------------*/
"""

class Usuario(object):
    """
    Representa a conta de uma pessoa.
    """
    def __init__(self, login, senha, nome, fichas=1000):
        self.login = login
        self.senha = senha
        self.nome = nome
        self.fichas = fichas

    def get_usuario(self):
        usuario = (self.login, self.senha, self.nome, self.fichas)
        return usuario
