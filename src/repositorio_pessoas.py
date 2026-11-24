"""Contrato para definição de responsabilidades"""
from abc import ABC, abstractmethod
from pessoa import Pessoa

class RepositorioPessoas(ABC):
    @abstractmethod
    def cadastrar(self, pessoa): pass

    @abstractmethod
    def buscar(self, nome): pass

    @abstractmethod
    def listar(self): pass

    @abstractmethod
    def alterar(self, nome: str, nova_pessoa: Pessoa) -> bool:
        pass

    @abstractmethod
    def remover(self, nome):
        """Remove uma pessoa pelo nome."""
        passs