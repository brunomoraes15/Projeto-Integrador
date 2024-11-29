
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

SQL_DROP_TABLE = """
DROP TABLE IF EXISTS usuario
"""

SQL_INSERIR_USUARIO = """
INSERT INTO usuario (nome, data_nascimento, email, cpf, telefone, endereco, senha, tipo_usuario)
VALUES (?, ?, ?, ?, ?, ?, ?, ?);
"""


SQL_VERIFICAR_USUARIO = """
SELECT * FROM usuario
WHERE email = ? AND senha = ?
"""

ALTERAR_NOME = """
UPDATE usuario
SET nome = ?
WHERE email = ?;
"""

DELETAR_USER = """
DELETE FROM usuario
WHERE email = ?;
"""
