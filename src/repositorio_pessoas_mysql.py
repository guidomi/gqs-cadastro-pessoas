import mysql.connector
from repositorio_pessoas import RepositorioPessoas
from pessoa import Pessoa

class RepositorioPessoasMySQL(RepositorioPessoas):
    def __init__(self):
        self.__conexao = mysql.connector.connect(
            host="127.0.0.1",
            port=3307,
            user="root",
            password="root_lab_2026"
        )
        self.__cursor = self.__conexao.cursor()
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS cadastro")
        self.__conexao.database = "cadastro"
        self.__criar_tabela()

    def __criar_tabela(self):
        sql = """
        CREATE TABLE IF NOT EXISTS pessoa (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            idade INT NOT NULL,
            email VARCHAR(100) NOT NULL
        )
        """
        self.__cursor.execute(sql)
        self.__conexao.commit()

    def cadastrar(self, pessoa):
        sql = "INSERT INTO pessoa (nome, idade, email) VALUES (%s, %s, %s)"
        valores = (pessoa.getNome(), pessoa.getIdade(), pessoa.getEmail())
        self.__cursor.execute(sql, valores)
        self.__conexao.commit()
        return True

    def buscar(self, nome):
        sql = "SELECT nome, idade, email FROM pessoa WHERE nome = %s"
        # ...
        self.__cursor.execute(sql, (nome,))
        resultado = self.__cursor.fetchone()
        if resultado:
            return Pessoa(resultado[0], resultado[1], resultado[2])
        return None

    def listar(self):
        sql = "SELECT nome, idade, email FROM pessoa"
        self.__cursor.execute(sql)
        resultados = self.__cursor.fetchall()
        pessoas = []
        for res in resultados:
            pessoas.append(Pessoa(res[0], res[1], res[2]))
        return pessoas

    def alterar(self, nome, nova_pessoa):
        sql = "UPDATE pessoa SET nome = %s, idade = %s, email = %s WHERE nome = %s"
        valores = (nova_pessoa.getNome(), nova_pessoa.getIdade(), nova_pessoa.getEmail(), nome)
        self.__cursor.execute(sql, valores)
        self.__conexao.commit()
        return self.__cursor.rowcount > 0

    def remover(self, nome):
        sql = "DELETE FROM pessoa WHERE nome = %s"
        self.__cursor.execute(sql, (nome,))
        self.__conexao.commit()
        return self.__cursor.rowcount > 0