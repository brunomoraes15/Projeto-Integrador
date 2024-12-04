import sqlite3
from typing import Optional
from UsuarioQuery import * 
from encript import * 
from ConsultaQuery import *
from mensagens import *

class BancoDeDados:
    def __init__(self):
        self.path = 'database/database.db'
        self.conexao_banco = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexao_banco = sqlite3.connect(self.path)
            self.conexao_banco.row_factory = sqlite3.Row
            self.cursor = self.conexao_banco.cursor()
        except Exception as inst:
            print(f"Erro ao conectar no banco de dados: {inst}")
            
    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao_banco:
            self.conexao_banco.close()

    def criar_banco(self) -> bool:
        try:
            self.conectar()
            self.cursor.execute(SQL_CRIAR_CONSULTA)
            self.conexao_banco.commit()
            return self.cursor.rowcount > 0
        except Exception as inst:
            print(f'Erro ao criar a tabela no banco de dados: {inst}') 
            return False 
        finally:
            self.desconectar()

    def limpar_banco(self) -> bool:
        try:
            self.conectar()
            self.cursor.execute(SQL_DROPAR_TABLE)
            self.conexao_banco.commit()
            return self.cursor.rowcount > 0   
        except Exception as inst:
            print(f"Erro ao atualizar dados no banco de dados: {inst}")
            return False  
        finally:
            self.desconectar()

    def obter_senha_por_email(self, email: str) -> Optional[str]:
        try:
            self.conectar()
            self.cursor.execute(SQL_OBTER_SENHA_POR_EMAIL, (email,))
            dados = self.cursor.fetchone() 
            if dados is None:
                return None
            return dados["senha"]  
        except Exception as inst:
            print(f'Erro ao obter senha do banco de dados: {inst}')
        finally:
            self.desconectar()

    def obter_dados_por_email(self, email: str) -> Optional[Usuario]:
        try:
            self.conectar()
            self.cursor.execute(SQL_OBTER_DADOS_POR_EMAIL, (email,))
            dados = self.cursor.fetchone()  
            if dados is None:
                return None
            return Usuario(**dados)  
        except Exception as inst:
            print(f'Erro ao obter dados do banco de dados: {inst}')
        finally:
            self.desconectar()
    
    def cadastrar_usuario(self, user: Usuario) -> bool:
        try:
            self.conectar()
            self.cursor.execute(
                SQL_INSERIR_USUARIO,
                (
                    user.nome,
                    user.data_nascimento,
                    user.email,
                    user.cpf,
                    user.telefone,
                    user.endereco,
                    user.senha,
                    user.tipo_usuario
                )
            )
            self.conexao_banco.commit()
            return self.cursor.rowcount > 0   
        except Exception as inst:
            print(f"Erro ao inserir dados no banco de dados: {inst}")
            return False  
        finally:
            self.desconectar()
            
    def verificar_usuario(self, email: str, senha: str) -> bool:
        try:
            self.conectar()
            self.cursor.execute(SQL_VERIFICAR_USUARIO, (email, senha))
            resultado = self.cursor.fetchone()
            return bool(resultado)  
        except Exception as inst:
            print(f"Erro ao verificar o usuário no banco de dados: {inst}")
            return False
        finally:
            self.desconectar()
            
    def buscar_usuario(self, email: str) -> bool:
        try:
            self.conectar()
            self.cursor.execute(SQL_BUSCAR_USUARIO, (email,))
            resultado = self.cursor.fetchone()
            return bool(resultado)
        except Exception as inst:
            print(f"Erro ao buscar o usuário no banco de dados: {inst}")
            return False
        finally:
            self.desconectar()

    def atualizar_usuario(self, dados: dict) -> bool:
        try:
            self.conectar()
            self.cursor.execute(
                SQL_ATUALIZAR,
                (
                    dados.nome,
                    dados.email,-
                    dados.data_nascimento,
                    dados.cpf,
                    dados.telefone,
                    dados.endereco,
                    dados.senha,
                    dados.id
                )
            )
            self.conexao_banco.commit()
            return self.cursor.rowcount > 0   
        except Exception as inst:
            print(f"Erro ao atualizar dados no banco de dados: {inst}")
            return False  
        finally:
            self.desconectar()          
    
    def deletar_usuario(self, id_usuario: int):
        try:
            self.conectar()
            self.cursor.execute(SQL_DELETAR_USER, (id_usuario,))
            self.conexao_banco.commit()
            return self.cursor.rowcount > 0   
        except Exception as inst:
            print(f"Erro ao deletar usuario no banco de dados: {inst}")
            return False  
        finally:
            self.desconectar()

    # Métodos relativos apenas às consultas
    
    def criar_checkup(self):
        try:
            self.conectar()
            self.cursor.execute(SQL_CRIAR_CONSULTA)
            self.conexao_banco.commit()   
        except Exception as inst:
            print(f'Erro ao criar tabela consulta: {inst}')  
        finally:
            self.desconectar()

    def registrar_checkup(self, checkup: Checkup) -> bool:
        try:
            self.conectar()
            self.cursor.execute(
                SQL_REGISTRAR_CONSULTA,
                (   
                    checkup.id_usuario,
                    checkup.nome_usuario,
                    checkup.febre,
                    checkup.dorCabeca,
                    checkup.fadiga,
                    checkup.faltaAr,
                    checkup.palpitacoes,
                    checkup.tontura,
                    checkup.perdaApetite,
                    checkup.nausea,
                    checkup.vomito,
                    checkup.perdaPeso,
                    checkup.dorAbdomen,
                    checkup.tosse,
                    checkup.descricaoSintomas
                )
            )
            self.conexao_banco.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            print(f"Erro ao registrar check-up: {e}")
            return False
        finally:
            self.desconectar()
            
    def buscar_checkup(self, id_check: int) -> Optional[Checkup]:
        try:
            self.conectar()
            self.cursor.execute(SQL_BUSCAR_CONSULTA, (id_check,))

            dados = self.cursor.fetchone()

            if dados is None:
                return None

            return Checkup(
            id=dados[0],               
            id_usuario=dados[1],        
            nome_usuario=dados[2],      
            febre=dados[3],
            dorCabeca=dados[4],
            fadiga=dados[5],
            faltaAr=dados[6],
            palpitacoes=dados[7],
            tontura=dados[8],
            perdaApetite=dados[9],
            nausea=dados[10],
            vomito=dados[11],
            perdaPeso=dados[12],
            dorAbdomen=dados[13],
            tosse=dados[14],
            descricaoSintomas=dados[15],
            diagnostico=dados[16]
)


        except Exception as inst:
            print(f"Erro ao coletar dados do banco de dados: {inst}")
            return None

        finally:
            self.desconectar()
            
    def buscar_todos_ids(self) -> dict:
        try:
            self.conectar() 
            self.cursor.execute(SQL_BUSCAR_TODOS_IDS)
            
            
            dados = self.cursor.fetchall() 
            
            # Se não encontrar dados, retorna um dicionário vazio
            if not dados:
                return {}
            
            # Cria um dicionário id: nome_usuario
            resultado = {registro[0]: registro[1] for registro in dados}
            
            return resultado
        
        except Exception as inst:
            print(f'Erro ao coletar os IDs e nomes de usuário do banco de dados: {inst}')
            return {}  # Retorna um dicionário vazio em caso de erro
        
        finally:
            self.desconectar()  # Sempre desconecta após a execução
            
    def inserir_diagnostico(self, checkup_id: int, diagnostico: str) -> bool:
            try:
                self.conectar()
                self.cursor.execute(SQL_INSERIR_DIAGNOSTICO, (diagnostico, checkup_id))
                self.conexao_banco.commit()

                if self.cursor.rowcount == 0:
                    return False
                return True
            except Exception as inst:
                print(f'Erro ao inserir diagnóstico no banco de dados: {inst}')
                return False
            finally:
                self.desconectar()

    def buscar_consultas_por_ids(self,id_usuario: int) -> dict:
        try:
            self.conectar()  # Estabelece a conexão com o banco de dados
            
            # Executa a consulta SQL para buscar todos os ids e nomes de usuários
            self.cursor.execute(SQL_BUSCAR_CONSULTA_POR_ID, (id_usuario,))
            
            # Obtém todos os resultados
            dados = self.cursor.fetchall()  # Retorna todas as linhas
            
            # Se não encontrar dados, retorna um dicionário vazio
            if not dados:
                return {}
            
            # Cria um dicionário id: nome_usuario
            resultado = {registro[0]: registro[1] for registro in dados}
            
            return resultado
        
        except Exception as inst:
            print(f'Erro ao coletar os IDs e nomes de usuário do banco de dados: {inst}')
            return {}  # Retorna um dicionário vazio em caso de erro
        
        finally:
            self.desconectar()  # Sempre desconecta após a execução


# Teste de usuário
adm = Usuario(
    nome="admin",
    email="administrador@system",
    senha=cript("admin"),
    tipo_usuario="admin"
)

usuario_teste = Usuario(
    nome="Marjory Novato",
    data_nascimento="2008-06-13",
    email="marjory@dominio.com",
    senha=cript("senha123"),  
    cpf="12345678901",
    telefone="31987654321",
    endereco="Rua A, 123 - Bairro Exemplo, Cidade/UF",
    tipo_usuario="cliente"
)

medico_teste = Usuario(
    nome="Doutor",
    data_nascimento="2008-06-13",
    email="farofaCorporation@dominio.com",
    senha=cript("senha123"),  
    cpf="12345678901",
    telefone="31987654321",
    endereco="Rua A, 123 - Bairro Exemplo, Cidade/UF",
    tipo_usuario="medico"
)
