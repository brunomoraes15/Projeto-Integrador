# Arquivo com Queries relativas ao usuario

from dataclasses import dataclass
from typing import Optional


@dataclass
class Usuario:
    id: Optional[int] = None
    nome: Optional[str] = None
    data_nascimento: Optional[str] = None
    email: Optional[str] = None
    senha: Optional[str] = None
    cpf: Optional[str] = None
    telefone: Optional[int] = None
    endereco: Optional[str] = None
    tipo_usuario: Optional[str] = None


SQL_INSERIR = """
   INSERT INTO usuario (nome, email) 
   VALUES (?, ?)
"""

SQL_CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    data_nascimento DATE,
    email TEXT NOT NULL,
    cpf TEXT,
    telefone INTEGER,
    endereco TEXT,
    senha TEXT NOT NULL,
    tipo_usuario TEXT NOT NULL
);
"""

SQL_LIMPAR_TABLE = """
DELETE FROM usuario;
"""

SQL_DROPAR_TABLE = """
DROP TABLE IF EXISTS consultas;
"""

SQL_INSERIR_USUARIO = """
INSERT INTO usuario (nome, data_nascimento, email, cpf, telefone, endereco, senha, tipo_usuario)
VALUES (?, ?, ?, ?, ?, ?, ?, ?);
"""


SQL_VERIFICAR_USUARIO = """
SELECT * FROM usuario
WHERE email = ? AND senha = ?
"""

SQL_BUSCAR_USUARIO = """
SELECT * FROM usuario
WHERE email = ?
"""


SQL_ALTERAR_NOME = """
UPDATE usuario
SET nome = ?
WHERE email = ?;
"""

SQL_DELETAR_USER = """
DELETE FROM usuario
WHERE id = ?;
"""


SQL_ATUALIZAR = """
UPDATE usuario
SET 
nome = ?,
email = ?,
data_nascimento = ?,
cpf = ?,
telefone = ?,
endereco = ?,
senha = ?  
WHERE id = ?
            
"""








#foda
SQL_OBTER_SENHA_POR_EMAIL = """
        SELECT senha
        FROM usuario
        WHERE email = ?
    """
    
SQL_OBTER_DADOS_POR_EMAIL = """
    SELECT *
    FROM usuario
    WHERE email = ?
"""