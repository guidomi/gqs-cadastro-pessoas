from pessoa import Pessoa

class CadastroPessoas:
    def __init__(self, repositorio):
        self.__repositorio = repositorio

    def cadastrar(self, nome, idade, email):
        nova_pessoa = Pessoa(nome, idade, email)
        return self.__repositorio.cadastrar(nova_pessoa)

    def buscarPorNome(self, nome):
        return self.__repositorio.buscarPorNome(nome)

    def listar(self):
        return self.__repositorio.listar()

    def alterar(self, nome, novo_nome, nova_idade, novo_email):
        pessoa = self.buscarPorNome(nome)
        if pessoa is None:
            return None

        nova_pessoa = Pessoa(novo_nome, nova_idade, novo_email)

        if self.__repositorio.alterar(nome, nova_pessoa):
            return nova_pessoa
        return None

    def remover(self, nome):
        return self.__repositorio.remover(nome)