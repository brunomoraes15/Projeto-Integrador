import psycopg2
from config import *

# PostgreSQL connection class
class PostgreSQL:
    def __init__(self, host, dbname, user, password, port):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port
        self.conexao_banco = None
        self.cursor = None

    def conectar(self):
        self.conexao_banco = psycopg2.connect(
            host=self.host,
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            port=self.port
        )
        self.cursor = self.conexao_banco.cursor()

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao_banco:
            self.conexao_banco.close()


class Banco_de_Dados(PostgreSQL):
    def __init__(self, host, dbname, user, password, port):
        super().__init__(host, dbname, user, password, port)

    def inserir_usuario(self, email, senha):
        try:
            self.conectar()
            
            query = """
            INSERT INTO usuarios (email, senha) 
            VALUES (%s, %s)
            """
            
            self.cursor.execute(query, (email, senha))
            self.conexao_banco.commit()
            
        except Exception as inst:
            print(f'erro ao inserir dados no banco {inst}')  
             
        finally:
            self.desconectar()
bd = Banco_de_Dados(
        host=host,
        dbname=dbname,
        user=user,
        password=password,
        port=port
    )
bd.inserir_usuario('email', 'senha')