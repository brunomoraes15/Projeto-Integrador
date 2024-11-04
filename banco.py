import psycopg2
from dataclasses import dataclass
from typing import Optional
from queries import *


db_user='postgres.mrdtrwwuuygncapsfkix' 
password =  '9CrUhzi!ey??8jF' 
host='aws-0-sa-east-1.pooler.supabase.com' 
port='6543' 
dbname='postgres'

"""
# old shit
db_user = 'postgres'
password = 'bd'
host = 'localhost'
port = '5432'  
dbname = "SusNet"

"""
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
    def __init__(self, host, dbname, user, password, port):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port
        self.conexao_banco = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexao_banco = psycopg2.connect(
                host=self.host,
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                port=self.port
            )
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



'''new_user = Usuario(
    email="sabotagem@gmail",
    senha="Sabotagem da Silva Junior"
)

bd = BancoDeDados(
    host=host,
    dbname=dbname,
    user=db_user, 
    password=password,
    port=port
)

bd.drop_banco()
bd.criar_banco()
print(new_user)
print(new_user.email, new_user.senha)
bd.inserir_usuario_registro(new_user)
'''