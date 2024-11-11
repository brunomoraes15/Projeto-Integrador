from dataclasses import dataclass
from typing import Optional
import sqlite3
from queries import *

@dataclass
class Usuario:
    id:         Optional[int] = None
    nome:       Optional[str] = None
    email:      Optional[str] = None
    senha:      Optional[str] = None
    cpf:        Optional[str] = None
    telefone:   Optional[int] = None
    endereco:   Optional[str] = None

class BancoDeDados:
    def __init__(self):
        self.path = 'database/database.db'
        self.conexao_banco = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexao_banco = sqlite3.connect(self.path)
            self.cursor = self.conexao_banco.cursor()
        except Exception as inst:
            print(f"Erro ao conectar no banco de dados: {inst}")
            
    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao_banco:
            self.conexao_banco.close()
            
    def criar_banco(self):
        try:
            self.conectar()
            #self.cursor.execute(SQL_DROP_TABLE)
            self.cursor.execute(SQL_CRIAR_TABELA)
            self.conexao_banco.commit()
        except Exception as inst:
            print(f'Erro ao criar a tabela no banco de dados: {inst}')  
        finally:
            self.desconectar()
            
    def inserir_usuario_registro(self, user: Usuario):
        try:
            self.conectar()
            self.cursor.execute(SQL_INSERIR_REGISTRAR, (user.email, user.senha))
            self.conexao_banco.commit()
        except Exception as inst:
            print(f'Erro ao inserir dados no banco de dados: {inst}')  
        finally:
            self.desconectar()
            
    def verificar_usuario(self, email: str, senha: str):
        try:
            self.conectar()
            self.cursor.execute(SQL_VERIFICAR_USUARIO, (email, senha))
            return self.cursor.fetchone()  
        except Exception:
            return None
        finally:
            self.desconectar()

    def drop_banco(self):
        try:
            self.conectar()
            self.cursor.execute(SQL_DROP_TABLE)
            self.conexao_banco.commit()   
        except Exception as inst:
            print(f'Erro ao dropar tabela no banco de dados: {inst}')  
        finally:
            self.desconectar()


# Instancia a classe BancoDeDados e cria a tabela
bd = BancoDeDados()
bd.criar_banco()

# Teste de inserção de usuário
novo_usuario = Usuario(email="exemplo@dominio.com", senha="senha123")
print(f"Inserindo usuário: {novo_usuario.email}")
bd.inserir_usuario_registro(novo_usuario)
