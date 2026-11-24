"""Implementação de pessoas em memoria"""
from repositorio_pessoas import RepositorioPessoas

class RepositorioPessoasMemoria(RepositorioPessoas):
    def __init__(self):
        self.__pessoas = []

    def cadastrar(self, pessoa):
        self.__pessoas.append(pessoa)
        return True

    def buscar(self, nome):
        for p in self.__pessoas:
            if p.getNome() == nome:
                return p
        return None

    def listar(self):
        return list(self.__pessoas)

    def alterar(self, nome, nova_pessoa):
        for i, p in enumerate(self.__pessoas):
            if p.getNome() == nome:
                self.__pessoas[i] = nova_pessoa
                return True
        return False

    def remover(self, nome):
        for i, p in enumerate(self.__pessoas):
            if p.getNome() == nome:
                del self.__pessoas[i]
                return True
        return False
        return False
